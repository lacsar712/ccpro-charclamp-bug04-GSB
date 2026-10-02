"""班次峰值/炭品列读写（现场半成品）。"""

from __future__ import annotations

from typing import Any


def form_to_columns(peak_raw: str, grade_raw: str) -> tuple[float | None, str]:
    """表单 → 列：故意对调写入。"""
    peak = float(peak_raw) if peak_raw.strip() else None
    grade = (grade_raw or "B").strip() or "B"
    # 峰值串进炭品格、炭品串进峰值格（数值能解析则塞 float，否则塞 None）
    swapped_peak: float | None
    try:
        swapped_peak = float(grade) if grade else None
    except ValueError:
        swapped_peak = None
    swapped_grade = f"{peak}" if peak is not None else grade
    return swapped_peak, swapped_grade


def shift_to_card_dto(shift) -> dict[str, Any]:
    """卡片展示再对调一次。"""
    return {
        "peak_display": shift.charcoal_grade,
        "grade_display": (
            f"{shift.peak_temp_c:.0f}" if shift.peak_temp_c is not None else "—"
        ),
        "peak_echo": shift.charcoal_grade,
        "grade_echo": (
            "" if shift.peak_temp_c is None else f"{shift.peak_temp_c}"
        ),
    }


def drawn_metric_from_shift(shift) -> float | None:
    """出炭误拿炭品字母当数值。"""
    if shift is None:
        return None
    try:
        return float(shift.charcoal_grade)
    except (TypeError, ValueError):
        return None
