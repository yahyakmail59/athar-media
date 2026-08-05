# -*- coding: utf-8 -*-
"""Database models for the Athar Media website.

Content is bilingual: every translatable field exists as ``*_ar`` and ``*_en``.
A small ``_localized`` helper returns the right value based on the active
language, so templates can simply use ``{{ service.title }}``.
"""

from io import BytesIO
from pathlib import Path

from django.core.files.base import ContentFile
from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language

from PIL import Image, ImageOps


def _localized(ar_value, en_value):
    """Return the Arabic or English value depending on the active language."""
    lang = get_language() or "ar"
    if lang.startswith("ar"):
        return ar_value or en_value
    return en_value or ar_value


# Portfolio covers are drawn into a 4:3 card (`.work` sets aspect-ratio and
# `object-fit: cover`), so the browser crops whatever it is given. Doing that
# crop here instead means the stored file is exactly what the card shows, at
# twice the card's size so it stays sharp on phones.
COVER_WIDTH = 800
COVER_HEIGHT = 600
COVER_QUALITY = 76


def _normalise_cover(uploaded, basename):
    """Crop an upload to the card's 4:3 shape and re-encode it as WebP.

    Whatever comes out of a phone or a designer's export — a 6 MB portrait
    JPEG, a PNG with transparency, a photo rotated only by its EXIF tag —
    reaches the page as one predictable file, so adding a project never
    means resizing anything by hand first.
    """
    image = Image.open(uploaded)
    # Phone cameras record rotation in EXIF rather than in the pixels, and
    # Pillow reads the pixels, so this has to be applied before cropping.
    image = ImageOps.exif_transpose(image)

    if image.mode in ("RGBA", "LA", "P"):
        # WebP keeps alpha, but a transparent cover would show the card's navy
        # through it, so transparency is flattened onto white instead.
        image = image.convert("RGBA")
        flattened = Image.new("RGB", image.size, (255, 255, 255))
        flattened.paste(image, mask=image.split()[-1])
        image = flattened
    else:
        image = image.convert("RGB")

    # `ImageOps.fit` crops to the target ratio from the centre and scales in
    # one step, which is what `object-fit: cover` does in the browser.
    image = ImageOps.fit(
        image, (COVER_WIDTH, COVER_HEIGHT), method=Image.LANCZOS, centering=(0.5, 0.5),
    )

    buffer = BytesIO()
    image.save(buffer, "WEBP", quality=COVER_QUALITY, method=6)
    return ContentFile(buffer.getvalue(), name=f"{Path(basename).stem}.webp")


# Shared category choices for projects / portfolio filtering.
CATEGORY_CHOICES = [
    ("restaurant", "مطاعم"),
    ("clinic", "عيادات"),
    ("store", "متاجر"),
    ("cafe", "كافيهات"),
    ("other", "أخرى"),
]

# Icon keys map to inline SVG icons rendered in the templates.
ICON_CHOICES = [
    ("web", "تصميم مواقع"),
    ("ads", "إعلانات ممولة"),
    ("social", "سوشيال ميديا"),
    ("branding", "هوية بصرية"),
    ("seo", "تحسين محركات البحث"),
    ("content", "كتابة محتوى"),
    ("design", "تصميم جرافيك"),
    ("analytics", "تحليلات وتقارير"),
    ("photo", "تصوير منتجات"),
    ("store", "متاجر إلكترونية"),
]


class SiteSettings(models.Model):
    """Singleton holding contact details and social links (editable in admin)."""

    phone = models.CharField("الهاتف", max_length=40, default="+970 59 000 0000")
    whatsapp = models.CharField(
        "واتساب (بصيغة دولية بدون +)",
        max_length=40,
        default="970590000000",
        help_text="مثال: 970590000000",
    )
    email = models.EmailField("البريد الإلكتروني", default="info@atharmedia.ps")

    address_ar = models.CharField("العنوان (عربي)", max_length=200, default="غزة، فلسطين")
    address_en = models.CharField("العنوان (إنجليزي)", max_length=200, default="Gaza, Palestine")

    working_hours_ar = models.CharField(
        "ساعات العمل (عربي)", max_length=120, default="السبت - الخميس: 9 ص - 6 م"
    )
    working_hours_en = models.CharField(
        "ساعات العمل (إنجليزي)", max_length=120, default="Sat - Thu: 9 AM - 6 PM"
    )

    facebook = models.URLField("فيسبوك", blank=True)
    instagram = models.URLField("إنستغرام", blank=True)
    tiktok = models.URLField("تيك توك", blank=True)
    whatsapp_channel = models.URLField("قناة واتساب", blank=True)
    linkedin = models.URLField("لينكدإن", blank=True)
    youtube = models.URLField("يوتيوب", blank=True)
    x_twitter = models.URLField("X (تويتر)", blank=True)

    map_embed = models.TextField(
        "رابط تضمين الخريطة (Google Maps src)",
        blank=True,
        help_text="ضع رابط src من خريطة جوجل (Embed). اختياري.",
    )

    class Meta:
        verbose_name = "إعدادات الموقع"
        verbose_name_plural = "إعدادات الموقع"

    def __str__(self):
        return "إعدادات الموقع"

    def save(self, *args, **kwargs):
        self.pk = 1  # enforce singleton
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    @property
    def address(self):
        return _localized(self.address_ar, self.address_en)

    @property
    def working_hours(self):
        return _localized(self.working_hours_ar, self.working_hours_en)

    @property
    def whatsapp_link(self):
        digits = "".join(c for c in (self.whatsapp or "") if c.isdigit())
        return f"https://wa.me/{digits}" if digits else ""

    @property
    def social_links(self):
        """Yield (name, url, icon_key) for every social link that is set."""
        candidates = [
            ("facebook", self.facebook, "facebook"),
            ("instagram", self.instagram, "instagram"),
            ("tiktok", self.tiktok, "tiktok"),
            ("whatsapp", self.whatsapp_channel, "whatsapp"),
            ("linkedin", self.linkedin, "linkedin"),
            ("youtube", self.youtube, "youtube"),
            ("x_twitter", self.x_twitter, "x"),
        ]
        return [(name, url, icon) for name, url, icon in candidates if url]


class Service(models.Model):
    title_ar = models.CharField("العنوان (عربي)", max_length=120)
    title_en = models.CharField("العنوان (إنجليزي)", max_length=120)
    short_ar = models.CharField("وصف مختصر (عربي)", max_length=240)
    short_en = models.CharField("وصف مختصر (إنجليزي)", max_length=240)
    description_ar = models.TextField("الوصف الكامل (عربي)", blank=True)
    description_en = models.TextField("الوصف الكامل (إنجليزي)", blank=True)

    icon = models.CharField("الأيقونة", max_length=20, choices=ICON_CHOICES, default="web")
    slug = models.SlugField("المعرّف (slug)", max_length=140, unique=True, blank=True)

    is_featured = models.BooleanField("مميّزة (تظهر بالرئيسية)", default=True)
    is_active = models.BooleanField("مفعّلة", default=True)
    order = models.PositiveIntegerField("الترتيب", default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "خدمة"
        verbose_name_plural = "الخدمات"
        ordering = ["order", "id"]

    def __str__(self):
        return self.title_ar

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title_en or self.title_ar, allow_unicode=True)
            self.slug = base or f"service-{self.pk or ''}"
        super().save(*args, **kwargs)

    @property
    def title(self):
        return _localized(self.title_ar, self.title_en)

    @property
    def short(self):
        return _localized(self.short_ar, self.short_en)

    @property
    def description(self):
        return _localized(self.description_ar, self.description_en)


class Project(models.Model):
    title_ar = models.CharField("اسم المشروع (عربي)", max_length=140)
    title_en = models.CharField("اسم المشروع (إنجليزي)", max_length=140)
    category = models.CharField("التصنيف", max_length=20, choices=CATEGORY_CHOICES, default="other")

    short_ar = models.CharField("وصف مختصر (عربي)", max_length=240, blank=True)
    short_en = models.CharField("وصف مختصر (إنجليزي)", max_length=240, blank=True)
    description_ar = models.TextField("الوصف (عربي)", blank=True)
    description_en = models.TextField("الوصف (إنجليزي)", blank=True)

    image = models.ImageField(
        "الصورة", upload_to="projects/", blank=True,
        help_text=(
            "أي مقاس وأي صيغة — تُقصّ تلقائيًا إلى 4:3 وتُحوَّل إلى WebP مضغوط. "
            "اتركها فارغة ليظهر الرسم التخطيطي التلقائي. "
            "ارفعها من لوحة التحكم على الموقع المنشور، لأن الصور المرفوعة محليًا لا تصل الخادم."
        ),
    )
    url = models.URLField("رابط الموقع/العمل", blank=True)
    client_name = models.CharField("اسم العميل", max_length=120, blank=True)
    year = models.CharField("السنة", max_length=8, blank=True)

    is_featured = models.BooleanField("مميّز (يظهر بالرئيسية)", default=False)
    is_active = models.BooleanField("منشور", default=True)
    order = models.PositiveIntegerField("الترتيب", default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "عمل / مشروع"
        verbose_name_plural = "الأعمال"
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title_ar

    def save(self, *args, **kwargs):
        # `_committed` is False only for a file that has just been assigned and
        # not yet written to storage, so an image is processed once on upload
        # rather than re-encoded on every edit of an unrelated field, which
        # would compress it again and again until it visibly degraded.
        if self.image and not self.image._committed:
            self.image = _normalise_cover(self.image, self.image.name)
        super().save(*args, **kwargs)

    @property
    def title(self):
        return _localized(self.title_ar, self.title_en)

    @property
    def short(self):
        return _localized(self.short_ar, self.short_en)

    @property
    def description(self):
        return _localized(self.description_ar, self.description_en)

    @property
    def category_label_key(self):
        """UI translation key used in templates, e.g. 'filter_restaurant'."""
        return f"filter_{self.category}"


class Testimonial(models.Model):
    name = models.CharField("اسم العميل", max_length=120)
    business_ar = models.CharField("النشاط (عربي)", max_length=140, blank=True)
    business_en = models.CharField("النشاط (إنجليزي)", max_length=140, blank=True)
    content_ar = models.TextField("الرأي (عربي)")
    content_en = models.TextField("الرأي (إنجليزي)", blank=True)
    rating = models.PositiveSmallIntegerField("التقييم (1-5)", default=5)
    image = models.ImageField("صورة العميل", upload_to="testimonials/", blank=True)

    is_active = models.BooleanField("منشور", default=True)
    order = models.PositiveIntegerField("الترتيب", default=0)

    class Meta:
        verbose_name = "توصية عميل"
        verbose_name_plural = "آراء العملاء"
        ordering = ["order", "id"]

    def __str__(self):
        return self.name

    @property
    def business(self):
        return _localized(self.business_ar, self.business_en)

    @property
    def content(self):
        return _localized(self.content_ar, self.content_en)

    @property
    def stars_range(self):
        return range(1, 6)


class ContactMessage(models.Model):
    name = models.CharField("الاسم", max_length=120)
    email = models.EmailField("البريد الإلكتروني", blank=True)
    phone = models.CharField("رقم الهاتف", max_length=40)
    business_type = models.CharField("نوع النشاط", max_length=120, blank=True)
    service = models.ForeignKey(
        Service,
        verbose_name="الخدمة المطلوبة",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    message = models.TextField("الرسالة")

    is_read = models.BooleanField("تمت القراءة", default=False)
    created_at = models.DateTimeField("تاريخ الإرسال", auto_now_add=True)

    class Meta:
        verbose_name = "رسالة تواصل"
        verbose_name_plural = "رسائل التواصل"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.created_at:%Y-%m-%d}"
