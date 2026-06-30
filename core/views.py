# -*- coding: utf-8 -*-
"""Views for the Athar Media website."""

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm
from .i18n import get_ui
from .models import CATEGORY_CHOICES, Project, Service, Testimonial


def home(request):
    context = {
        "services": Service.objects.filter(is_active=True, is_featured=True)[:6],
        "all_services_count": Service.objects.filter(is_active=True).count(),
        "projects": Project.objects.filter(is_active=True, is_featured=True)[:6],
        "testimonials": Testimonial.objects.filter(is_active=True)[:6],
        "active_page": "home",
    }
    return render(request, "pages/home.html", context)


def services(request):
    context = {
        "services": Service.objects.filter(is_active=True),
        "active_page": "services",
    }
    return render(request, "pages/services.html", context)


def portfolio(request):
    cat = request.GET.get("cat", "all")
    valid = {key for key, _ in CATEGORY_CHOICES}
    projects = Project.objects.filter(is_active=True)
    if cat in valid:
        projects = projects.filter(category=cat)
    else:
        cat = "all"
    context = {
        "projects": projects,
        "categories": CATEGORY_CHOICES,
        "active_cat": cat,
        "active_page": "portfolio",
    }
    return render(request, "pages/portfolio.html", context)


def about(request):
    context = {
        "testimonials": Testimonial.objects.filter(is_active=True)[:6],
        "active_page": "about",
    }
    return render(request, "pages/about.html", context)


def contact(request):
    t = get_ui(request.lang)
    if request.method == "POST":
        form = ContactForm(request.POST, lang=request.lang)
        if form.is_valid():
            form.save()
            messages.success(request, t["form_success"])
            return redirect(reverse("core:contact"))
        messages.error(request, t["form_error"])
    else:
        form = ContactForm(lang=request.lang)

    context = {
        "form": form,
        "services": Service.objects.filter(is_active=True),
        "active_page": "contact",
    }
    return render(request, "pages/contact.html", context)


def set_language(request, lang):
    """Persist the chosen language in the session and return to the page."""
    codes = {code for code, _ in settings.LANGUAGES}
    if lang in codes:
        request.session["lang"] = lang
    next_url = request.META.get("HTTP_REFERER") or reverse("core:home")
    return redirect(next_url)
