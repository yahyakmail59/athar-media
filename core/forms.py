# -*- coding: utf-8 -*-
"""Forms for the Athar Media site."""

from django import forms

from .i18n import get_ui
from .models import CATEGORY_CHOICES, ContactMessage, Service


class ContactForm(forms.ModelForm):
    """Contact / quote-request form. Field labels & placeholders adapt to the
    active language, which is passed in from the view."""

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "business_type", "service", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }

    def __init__(self, *args, lang="ar", **kwargs):
        super().__init__(*args, **kwargs)
        t = get_ui(lang)

        # Bilingual business-type choices (shares the portfolio category keys).
        business_choices = [("", t["form_business"])]
        for key, _ar_label in CATEGORY_CHOICES:
            business_choices.append((t.get(f"filter_{key}", key), t.get(f"filter_{key}", key)))
        self.fields["business_type"] = forms.ChoiceField(
            choices=business_choices, required=False, label=t["form_business"]
        )

        # Only offer active services, with a localized empty label.
        self.fields["service"].queryset = Service.objects.filter(is_active=True)
        self.fields["service"].required = False
        self.fields["service"].empty_label = t["form_service_choose"]

        self.fields["email"].required = False
        self.fields["phone"].required = True

        # Localized labels
        self.fields["name"].label = t["form_name"]
        self.fields["email"].label = t["form_email"]
        self.fields["phone"].label = t["form_phone"]
        self.fields["service"].label = t["form_service"]
        self.fields["message"].label = t["form_message"]

        # Shared styling + placeholders
        placeholders = {
            "name": t["form_name"],
            "email": t["form_email"],
            "phone": t["form_phone"],
            "message": t["form_message"],
        }
        for name, field in self.fields.items():
            css = "form-control"
            if isinstance(field.widget, (forms.Select,)):
                css = "form-control form-select"
            field.widget.attrs.update({"class": css})
            if name in placeholders:
                field.widget.attrs["placeholder"] = placeholders[name]
