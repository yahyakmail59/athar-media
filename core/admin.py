# -*- coding: utf-8 -*-
"""Django admin configuration for Athar Media content management."""

from django.contrib import admin
from django.utils.html import format_html

from .models import ContactMessage, Project, Service, SiteSettings, Testimonial

admin.site.site_header = "أثر ميديا — لوحة التحكم"
admin.site.site_title = "أثر ميديا"
admin.site.index_title = "إدارة محتوى الموقع"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("معلومات التواصل", {"fields": ("phone", "whatsapp", "email")}),
        ("العنوان وساعات العمل", {
            "fields": ("address_ar", "address_en", "working_hours_ar", "working_hours_en"),
        }),
        ("روابط التواصل الاجتماعي", {
            "fields": ("facebook", "instagram", "tiktok", "whatsapp_channel",
                       "linkedin", "youtube", "x_twitter"),
        }),
        ("الخريطة", {"fields": ("map_embed",)}),
    )

    def has_add_permission(self, request):
        # Singleton: only one settings row allowed.
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title_ar", "title_en", "icon", "is_featured", "is_active", "order")
    list_editable = ("icon", "is_featured", "is_active", "order")
    list_filter = ("is_featured", "is_active", "icon")
    search_fields = ("title_ar", "title_en", "short_ar", "short_en")
    prepopulated_fields = {"slug": ("title_en",)}
    fieldsets = (
        ("العربية", {"fields": ("title_ar", "short_ar", "description_ar")}),
        ("English", {"fields": ("title_en", "short_en", "description_en")}),
        ("الإعدادات", {"fields": ("icon", "slug", "is_featured", "is_active", "order")}),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("thumb", "title_ar", "category", "client_name", "is_featured", "is_active", "order")
    list_display_links = ("thumb", "title_ar")
    list_editable = ("is_featured", "is_active", "order")
    list_filter = ("category", "is_featured", "is_active")
    search_fields = ("title_ar", "title_en", "client_name")
    fieldsets = (
        ("العربية", {"fields": ("title_ar", "short_ar", "description_ar")}),
        ("English", {"fields": ("title_en", "short_en", "description_en")}),
        ("التفاصيل", {"fields": ("category", "image", "url", "client_name", "year")}),
        ("الإعدادات", {"fields": ("is_featured", "is_active", "order")}),
    )

    @admin.display(description="الصورة")
    def thumb(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:42px;width:62px;object-fit:cover;border-radius:6px;" />',
                obj.image.url,
            )
        return "—"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "business_ar", "rating", "is_active", "order")
    list_editable = ("rating", "is_active", "order")
    list_filter = ("is_active", "rating")
    search_fields = ("name", "business_ar", "business_en")
    fieldsets = (
        ("العميل", {"fields": ("name", "image", "rating")}),
        ("العربية", {"fields": ("business_ar", "content_ar")}),
        ("English", {"fields": ("business_en", "content_en")}),
        ("الإعدادات", {"fields": ("is_active", "order")}),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "business_type", "service", "created_at", "is_read")
    list_editable = ("is_read",)
    list_filter = ("is_read", "created_at", "service")
    search_fields = ("name", "phone", "email", "message")
    readonly_fields = ("name", "email", "phone", "business_type", "service", "message", "created_at")
    date_hierarchy = "created_at"

    def has_add_permission(self, request):
        return False
