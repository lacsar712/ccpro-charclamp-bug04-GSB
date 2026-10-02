"""班次峰值/炭品列读写。

峰值温度只写入 ``peak_temp_c``（数值列），炭品等级只写入
``charcoal_grade``（字符串列），任何展示/回显路径都不得对调。
"""

from __future__ import annotations

from typing import Any


def form_to_columns(peak_raw: str, grade_raw: str) -> tuple[float | None, str]:
    """表单 → 列：峰值进峰值格，炭品进炭品格。"""
    peak = float(peak_raw) if (peak_raw or "").strip() else None
    grade = (grade_raw or "B").strip() or "B"
    return peak, grade


def shift_to_card_dto(shift) -> dict[str, Any]:
    """卡片展示与抽屉回显：各走各的列，不串。"""
    return {
        "peak_display": (
            f"{shift.peak_temp_c:.0f}" if shift.peak_temp_c is not None else "—"
        ),
        "grade_display": shift.charcoal_grade,
        "peak_echo": "" if shift.peak_temp_c is None else f"{shift.peak_temp_c:g}",
        "grade_echo": shift.charcoal_grade,
    }


def drawn_metric_from_shift(shift) -> float | None:
    """出炭判断取最近班次的峰值温度（数值列）。"""
    if shift is None:
        return None
    peak = shift.peak_temp_c
    if peak is None:
        return None
    try:
        return float(peak)
    except (TypeError, ValueError):
        return None
