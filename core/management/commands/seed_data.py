# -*- coding: utf-8 -*-
"""Populate the database with sample bilingual content so the site looks
complete out of the box. Safe to re-run (uses update_or_create).

Usage:  python manage.py seed_data
"""

from django.core.management.base import BaseCommand

from core.models import Project, Service, SiteSettings, Testimonial

SERVICES = [
    ("web", "تصميم وتطوير المواقع", "Web Design & Development",
     "مواقع عصرية سريعة ومتجاوبة مع جميع الأجهزة تعكس احترافية نشاطك.",
     "Modern, fast, responsive websites that reflect your business professionalism.",
     "نصمم ونطوّر مواقع إلكترونية احترافية متجاوبة مع الجوال، سريعة التحميل ومهيأة لمحركات البحث، تناسب المطاعم والعيادات والمتاجر والكافيهات.",
     "We design and build professional, mobile-responsive websites that load fast and are SEO-ready — perfect for restaurants, clinics, stores and cafés."),
    ("ads", "إدارة الإعلانات الممولة", "Paid Ads Management",
     "حملات إعلانية مدروسة على فيسبوك وإنستغرام تجلب لك عملاء حقيقيين.",
     "Well-targeted Facebook & Instagram campaigns that bring real customers.",
     "ندير حملاتك الإعلانية على منصات التواصل باستهداف دقيق لجمهورك المحلي في غزة، مع متابعة وتحسين مستمر للنتائج وعائد الإنفاق.",
     "We manage your social media ad campaigns with precise targeting of your local audience, with continuous optimization for the best return on ad spend."),
    ("social", "إدارة وسائل التواصل", "Social Media Management",
     "إدارة كاملة لحساباتك مع محتوى جذاب يبني علاقة مع جمهورك.",
     "Full account management with engaging content that builds your audience.",
     "نتولى إدارة حساباتك على السوشيال ميديا بالكامل: تخطيط المحتوى، التصميم، النشر، والتفاعل مع المتابعين لبناء حضور قوي لعلامتك.",
     "We fully manage your social media accounts: content planning, design, publishing and community engagement to build a strong brand presence."),
    ("branding", "الهوية البصرية", "Brand Identity",
     "شعار وهوية متكاملة تميّز علامتك التجارية وتترك أثراً في الأذهان.",
     "A complete logo & identity that makes your brand stand out and stick.",
     "نصمم هوية بصرية متكاملة تشمل الشعار والألوان والخطوط وكل عناصر علامتك التجارية لتظهر بشكل احترافي ومتناسق في كل مكان.",
     "We craft a complete visual identity — logo, colors, typography and all brand elements — so you look professional and consistent everywhere."),
    ("design", "تصميم الجرافيك", "Graphic Design",
     "تصاميم إبداعية للسوشيال ميديا والمطبوعات تلفت الأنظار.",
     "Creative designs for social media and print that grab attention.",
     "تصاميم احترافية لمنشورات السوشيال ميديا، البنرات، المنيو، والمطبوعات الدعائية بأسلوب يعكس هوية نشاطك.",
     "Professional designs for social posts, banners, menus and print materials in a style that reflects your brand."),
    ("store", "المتاجر الإلكترونية", "E-commerce Stores",
     "متجر إلكتروني متكامل لعرض منتجاتك واستقبال الطلبات أونلاين.",
     "A complete online store to showcase products and take orders online.",
     "نبني لك متجراً إلكترونياً سهل الاستخدام لعرض منتجاتك واستقبال الطلبات والدفع، مع لوحة تحكم بسيطة لإدارة كل شيء.",
     "We build an easy-to-use online store to showcase products, take orders and payments, with a simple dashboard to manage everything."),
    ("photo", "تصوير المنتجات", "Product Photography",
     "تصوير احترافي لمنتجاتك وأطباقك يبرز جودتها ويزيد المبيعات.",
     "Professional photography that highlights your products and boosts sales.",
     "نقدم خدمة تصوير احترافية للمنتجات والأطباق تبرز التفاصيل والجودة وتجعل عملاءك يرغبون بالشراء.",
     "We offer professional product and food photography that highlights detail and quality and makes customers want to buy."),
    ("content", "كتابة المحتوى", "Content Writing",
     "محتوى تسويقي مقنع يحكي قصة علامتك ويحفّز على التفاعل.",
     "Persuasive marketing content that tells your story and drives action.",
     "نكتب لك محتوى تسويقياً احترافياً باللغتين العربية والإنجليزية لمواقعك وإعلاناتك ومنشوراتك يجذب جمهورك ويحفّزه على اتخاذ القرار.",
     "We write professional marketing content in Arabic and English for your website, ads and posts that attracts and converts your audience."),
    ("seo", "تحسين محركات البحث", "SEO",
     "نجعل موقعك يظهر في النتائج الأولى على جوجل لعملائك المحتملين.",
     "We get your site to the top of Google for your potential customers.",
     "نحسّن موقعك ليظهر في النتائج الأولى لمحركات البحث عند بحث العملاء عن خدماتك، مما يزيد الزيارات والعملاء بشكل مستمر.",
     "We optimize your site to rank at the top of search results when customers look for your services, driving steady traffic and leads."),
    ("analytics", "التحليلات والتقارير", "Analytics & Reports",
     "تقارير دورية واضحة تقيس أداء حملاتك وتطوّر نتائجك.",
     "Clear periodic reports that measure performance and improve results.",
     "نزوّدك بتقارير دورية مفصلة عن أداء موقعك وحملاتك الإعلانية مع توصيات عملية لتحسين النتائج وزيادة العائد.",
     "We provide detailed periodic reports on your website and campaign performance, with practical recommendations to improve results."),
]

PROJECTS = [
    ("restaurant", "مطعم البحر", "Sea Restaurant", "موقع وقائمة طعام رقمية", "Website & digital menu", "مطعم البحر", "2025", True),
    ("clinic", "عيادة الابتسامة", "Smile Dental Clinic", "موقع حجز مواعيد للعيادة", "Clinic booking website", "عيادة الابتسامة", "2025", True),
    ("store", "متجر الأناقة", "Elegance Store", "متجر إلكتروني للأزياء", "Fashion e-commerce store", "متجر الأناقة", "2024", True),
    ("cafe", "كافيه لاتيه", "Latte Café", "هوية بصرية وحملة إعلانية", "Branding & ad campaign", "كافيه لاتيه", "2025", True),
    ("restaurant", "مطعم الذواقة", "Gourmet Restaurant", "إدارة سوشيال ميديا وإعلانات", "Social media & ads", "مطعم الذواقة", "2024", True),
    ("store", "متجر التقنية", "Tech Store", "متجر إلكتروني وتصوير منتجات", "Online store & product shots", "متجر التقنية", "2024", True),
]

TESTIMONIALS = [
    ("أحمد سمير", "صاحب مطعم", "Restaurant owner",
     "فريق أثر ميديا نقل مطعمي لمستوى آخر! الموقع رائع والإعلانات جابتلنا زبائن كثير. شكراً على الاحترافية.",
     "Athar Media took my restaurant to another level! The website is great and the ads brought us many customers.", 5),
    ("د. ليلى حسن", "طبيبة أسنان", "Dentist",
     "تعاملت معهم على تصميم موقع العيادة ونظام الحجز، النتيجة فاقت توقعاتي والمتابعة ممتازة.",
     "I worked with them on the clinic website and booking system; the result exceeded my expectations.", 5),
    ("محمود العبد", "صاحب متجر", "Store owner",
     "أفضل قرار اتخذته لمشروعي. متجر إلكتروني احترافي وتصوير منتجات خرافي زاد مبيعاتي بشكل ملحوظ.",
     "The best decision for my business. A professional online store and amazing product photos boosted my sales.", 5),
]


class Command(BaseCommand):
    help = "Seed the database with sample bilingual content for Athar Media."

    def handle(self, *args, **options):
        # Site settings (singleton) with Gaza-friendly defaults + sample socials.
        site = SiteSettings.load()
        site.phone = site.phone or "+970 59 000 0000"
        if not site.facebook:
            site.facebook = "https://facebook.com/"
        if not site.instagram:
            site.instagram = "https://instagram.com/"
        site.save()
        self.stdout.write(self.style.SUCCESS("-Site settings ready"))

        for order, s in enumerate(SERVICES):
            icon, t_ar, t_en, sh_ar, sh_en, d_ar, d_en = s
            Service.objects.update_or_create(
                title_en=t_en,
                defaults=dict(
                    icon=icon, title_ar=t_ar, short_ar=sh_ar, short_en=sh_en,
                    description_ar=d_ar, description_en=d_en,
                    is_featured=order < 6, is_active=True, order=order,
                ),
            )
        self.stdout.write(self.style.SUCCESS(f"- {len(SERVICES)} services"))

        for order, p in enumerate(PROJECTS):
            cat, t_ar, t_en, sh_ar, sh_en, client, year, featured = p
            Project.objects.update_or_create(
                title_en=t_en,
                defaults=dict(
                    category=cat, title_ar=t_ar, short_ar=sh_ar, short_en=sh_en,
                    client_name=client, year=year, is_featured=featured,
                    is_active=True, order=order,
                ),
            )
        self.stdout.write(self.style.SUCCESS(f"- {len(PROJECTS)} projects"))

        for order, tt in enumerate(TESTIMONIALS):
            name, biz_ar, biz_en, c_ar, c_en, rating = tt
            Testimonial.objects.update_or_create(
                name=name,
                defaults=dict(
                    business_ar=biz_ar, business_en=biz_en, content_ar=c_ar,
                    content_en=c_en, rating=rating, is_active=True, order=order,
                ),
            )
        self.stdout.write(self.style.SUCCESS(f"- {len(TESTIMONIALS)} testimonials"))
        self.stdout.write(self.style.SUCCESS("Done! Visit http://127.0.0.1:8000/"))
