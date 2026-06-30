"""Template context processor — makes language, UI strings and site info
available to every template without repeating them in each view."""

from django.conf import settings

from .i18n import get_ui


def site_context(request):
    lang = getattr(request, "lang", settings.DEFAULT_LANGUAGE)

    # SiteSettings is a singleton holding contact info & social links.
    # Guarded so the site still renders before the first migration.
    site = None
    try:
        from .models import SiteSettings

        site = SiteSettings.load()
    except Exception:
        site = None

    return {
        "lang": lang,
        "text_dir": getattr(request, "text_dir", "rtl"),
        "is_rtl": lang == "ar",
        "t": get_ui(lang),
        "site": site,
        "site_languages": settings.LANGUAGES,
    }
