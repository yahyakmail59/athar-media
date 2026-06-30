"""Language middleware for the bilingual (ar/en) Athar Media site.

Reads the visitor's chosen language from the session, activates Django's
translation machinery (so ``get_language()`` works inside model properties),
and exposes ``request.lang`` / ``request.text_dir`` for views and templates.
"""

from django.conf import settings
from django.utils import translation


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self._codes = {code for code, _ in settings.LANGUAGES}

    def __call__(self, request):
        lang = request.session.get("lang", settings.DEFAULT_LANGUAGE)
        if lang not in self._codes:
            lang = settings.DEFAULT_LANGUAGE

        translation.activate(lang)
        request.lang = lang
        request.text_dir = "rtl" if lang == "ar" else "ltr"

        response = self.get_response(request)

        response["Content-Language"] = lang
        translation.deactivate()
        return response
