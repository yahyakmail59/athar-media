# -*- coding: utf-8 -*-
"""URL routes for the core app."""

from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("lang/<str:lang>/", views.set_language, name="set_language"),
]
