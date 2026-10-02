"""班次峰值/炭品列读写：峰值数值只进峰值格，炭品等级只进炭品格。"""

from __future__ import annotations

from typing import Any


def form_to_columns(peak_raw: str, grade_raw: str) -> tuple[float | None, str]:
    """表单 → 列（一一对应，不串列）。

    峰值温度表单值 → ``peak_temp_c`` 数值列（空则为 None）；
    炭品等级表单值 → ``charcoal_grade`` 文字列（空则默认 "B"）。
    """
    peak = float(peak_raw) if peak_raw and peak_raw.strip() else None
    grade = (grade_raw or "B").strip() or "B"
    return peak, grade


def shift_to_card_dto(shift) -> dict[str, Any]:
    """卡片展示与抽屉回显：峰值格显示数值峰值，炭品格显示炭品等级。"""
    peak = shift.peak_temp_c
    grade = shift.charcoal_grade
    return {
        "peak_display": f"{peak:.0f}" if peak is not None else "—",
        "grade_display": grade or "—",
        "peak_echo": "" if peak is None else f"{peak:g}",
        "grade_echo": grade or "",
    }


def drawn_metric_from_shift(shift) -> float | None:
    """出炭判断取数值峰值温度（peak_temp_c），不读炭品字母。"""
    if shift is None:
        return None
    return shift.peak_temp_c
