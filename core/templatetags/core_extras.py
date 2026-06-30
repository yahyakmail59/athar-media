# -*- coding: utf-8 -*-
"""Custom template helpers for Athar Media."""

from django import template

register = template.Library()


@register.filter
def dictkey(mapping, key):
    """Look up ``mapping[key]`` with a variable key (used for the UI string table)."""
    try:
        return mapping.get(key, "")
    except AttributeError:
        return ""


# Category-driven colours for the auto-generated project mockups.
_ACCENT = {
    "restaurant": "#E8853A",  # warm amber — food
    "cafe": "#B07A4F",        # caramel — coffee
    "clinic": "#1FA6B8",      # teal — medical/clean
    "store": "#0A4DBC",       # brand blue — retail
    "other": "#4A95D9",       # sky
}
_TINT = {
    "restaurant": "#0A4DBC",
    "cafe": "#062F57",
    "clinic": "#0A4DBC",
    "store": "#062F57",
    "other": "#0A4DBC",
}


@register.filter
def mk_accent(category):
    """Accent colour for a project mockup, based on its category."""
    return _ACCENT.get(category, _ACCENT["other"])


@register.filter
def mk_tint(category):
    """Banner gradient base colour for a project mockup."""
    return _TINT.get(category, _TINT["other"])
