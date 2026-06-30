# -*- coding: utf-8 -*-
"""Lightweight UI translation table for Athar Media.

All static interface strings live here in both Arabic and English. This avoids
the need to compile gettext ``.po`` files (which require external binaries on
Windows) while keeping the site fully bilingual and easy to extend.

Usage: a context processor injects ``t = get_ui(request.lang)`` so templates can
write ``{{ t.nav_home }}`` etc.
"""

UI = {
    "ar": {
        # Brand
        "brand_name": "أثر ميديا",
        "brand_tagline": "وكالة تسويق رقمي",
        "slogan": "نصنع أثراً رقمياً يَدوم",
        "slogan_sub": "نحوّل أفكار مشروعك إلى حضور رقمي يجذب العملاء ويزيد المبيعات",

        # Navigation
        "nav_home": "الرئيسية",
        "nav_services": "خدماتنا",
        "nav_portfolio": "أعمالنا",
        "nav_about": "من نحن",
        "nav_contact": "تواصل معنا",
        "nav_quote": "اطلب عرض سعر",
        "lang_switch": "English",
        "skip_to_content": "تخطَّ إلى المحتوى",

        # Hero
        "hero_badge": "خدماتنا داخل قطاع غزة",
        "hero_title": "نصنع لمشروعك أثراً رقمياً يَدوم",
        "hero_text": "تصميم مواقع إلكترونية احترافية وإدارة إعلانات تسويقية للمطاعم والعيادات والمتاجر والكافيهات — لنساعدك على الوصول لعملائك وزيادة مبيعاتك.",
        "hero_cta_primary": "ابدأ مشروعك الآن",
        "hero_cta_secondary": "شاهد أعمالنا",

        # Stats
        "stat_projects": "مشروع منجز",
        "stat_clients": "عميل سعيد",
        "stat_experience": "سنوات خبرة",
        "stat_support": "دعم متواصل",

        # Services
        "services_title": "خدماتنا",
        "services_subtitle": "حلول تسويقية رقمية متكاملة مصمّمة لنمو نشاطك التجاري",
        "services_cta": "اعرف المزيد",
        "services_all": "كل الخدمات",

        # Why us / Features
        "why_title": "لماذا أثر ميديا؟",
        "why_subtitle": "نجمع بين الإبداع والاحترافية لنقدّم لك نتائج حقيقية",
        "feature_1_title": "تصاميم عصرية",
        "feature_1_text": "هوية ومواقع بتصاميم حديثة تعكس احترافية علامتك التجارية.",
        "feature_2_title": "نتائج حقيقية",
        "feature_2_text": "حملات إعلانية مدروسة تستهدف عملاءك وتزيد مبيعاتك فعلياً.",
        "feature_3_title": "فريق محلي",
        "feature_3_text": "فريق من غزة يفهم سوقك المحلي ويتحدث لغة جمهورك.",
        "feature_4_title": "دعم متواصل",
        "feature_4_text": "نرافقك بعد التسليم بالمتابعة والدعم الفني المستمر.",

        # Process (how we work)
        "process_title": "كيف نعمل؟",
        "process_sub": "خطوات بسيطة وواضحة من الفكرة حتى الإطلاق",
        "step_1_title": "الاستشارة",
        "step_1_text": "نستمع لفكرتك ونفهم نشاطك وأهدافك وجمهورك المستهدف.",
        "step_2_title": "التخطيط والتصميم",
        "step_2_text": "نضع الاستراتيجية ونصمم الحلول المناسبة لعلامتك التجارية.",
        "step_3_title": "التنفيذ",
        "step_3_text": "نطوّر الموقع ونطلق الحملات الإعلانية باحترافية وإتقان.",
        "step_4_title": "المتابعة والتطوير",
        "step_4_text": "نحلل النتائج ونحسّن الأداء باستمرار لتحقيق أفضل عائد.",

        # Portfolio
        "portfolio_title": "أعمالنا",
        "portfolio_subtitle": "نماذج من المشاريع التي صنعنا فيها الفرق",
        "portfolio_view": "عرض المشروع",
        "portfolio_visit": "زيارة الموقع",
        "portfolio_empty": "سيتم إضافة الأعمال قريباً.",
        "filter_all": "الكل",
        "filter_restaurant": "مطاعم",
        "filter_clinic": "عيادات",
        "filter_store": "متاجر",
        "filter_cafe": "كافيهات",
        "filter_other": "أخرى",

        # Testimonials
        "testi_title": "ماذا قال عملاؤنا",
        "testi_subtitle": "ثقة عملائنا هي أثرنا الحقيقي",

        # CTA band
        "cta_band_title": "جاهز لتترك أثراً رقمياً؟",
        "cta_band_text": "تواصل معنا اليوم واحصل على استشارة مجانية لمشروعك.",
        "cta_band_button": "تواصل معنا الآن",

        # About page
        "about_title": "من نحن",
        "about_subtitle": "قصتنا ورسالتنا",
        "about_intro": "أثر ميديا وكالة تسويق رقمي من قلب غزة، متخصصة في تصميم المواقع الإلكترونية وإدارة الحملات الإعلانية للمطاعم والعيادات والمتاجر والكافيهات.",
        "about_story_title": "قصتنا",
        "about_story_text": "بدأنا برؤية بسيطة: مساعدة الأنشطة التجارية المحلية على النمو في العالم الرقمي. نؤمن أن كل مشروع يستحق حضوراً رقمياً يليق به، ونعمل على صناعة أثرٍ حقيقي يدوم لعملائنا.",
        "mission_title": "رسالتنا",
        "mission_text": "تمكين الأنشطة التجارية في غزة من الوصول لعملائها وزيادة مبيعاتها عبر حلول رقمية إبداعية واحترافية.",
        "vision_title": "رؤيتنا",
        "vision_text": "أن نكون الشريك الرقمي الأول للأنشطة التجارية المحلية، ونصنع لكل علامة تجارية أثراً يميّزها.",
        "values_title": "قيمنا",
        "value_1": "الإبداع",
        "value_2": "الاحترافية",
        "value_3": "الالتزام",
        "value_4": "الشفافية",

        # Contact page
        "contact_title": "تواصل معنا",
        "contact_subtitle": "أخبرنا عن مشروعك وسنعاود التواصل معك في أقرب وقت",
        "contact_info_title": "معلومات التواصل",
        "contact_phone": "الهاتف",
        "contact_email": "البريد الإلكتروني",
        "contact_address": "العنوان",
        "contact_hours": "ساعات العمل",
        "contact_whatsapp": "راسلنا على واتساب",
        "contact_follow": "تابعنا على",
        "form_name": "الاسم الكامل",
        "form_email": "البريد الإلكتروني",
        "form_phone": "رقم الهاتف",
        "form_business": "نوع النشاط",
        "form_service": "الخدمة المطلوبة",
        "form_service_choose": "اختر خدمة (اختياري)",
        "form_message": "رسالتك",
        "form_send": "إرسال الرسالة",
        "form_required": "هذا الحقل مطلوب",
        "form_success": "تم إرسال رسالتك بنجاح! سنتواصل معك قريباً.",
        "form_error": "حدث خطأ، يرجى مراجعة الحقول والمحاولة مرة أخرى.",

        # Footer
        "footer_about": "وكالة تسويق رقمي من غزة، نصمم المواقع وندير الحملات الإعلانية لنصنع لمشروعك أثراً يدوم.",
        "footer_links": "روابط سريعة",
        "footer_services": "خدماتنا",
        "footer_contact": "تواصل معنا",
        "footer_rights": "جميع الحقوق محفوظة",
        "footer_made": "صُنع بكل ❤ في غزة",
        "back_home": "العودة للرئيسية",
        "read_more": "اقرأ المزيد",
        "page_not_found": "الصفحة غير موجودة",
    },

    "en": {
        # Brand
        "brand_name": "Athar Media",
        "brand_tagline": "Digital Marketing Agency",
        "slogan": "Creating Digital Impact",
        "slogan_sub": "We turn your business ideas into a digital presence that attracts customers and grows sales",

        # Navigation
        "nav_home": "Home",
        "nav_services": "Services",
        "nav_portfolio": "Our Work",
        "nav_about": "About",
        "nav_contact": "Contact",
        "nav_quote": "Get a Quote",
        "lang_switch": "العربية",
        "skip_to_content": "Skip to content",

        # Hero
        "hero_badge": "Serving businesses across Gaza",
        "hero_title": "We create a digital impact that lasts",
        "hero_text": "Professional website design and marketing ad management for restaurants, clinics, stores and cafés — helping you reach your customers and grow your sales.",
        "hero_cta_primary": "Start your project",
        "hero_cta_secondary": "View our work",

        # Stats
        "stat_projects": "Projects delivered",
        "stat_clients": "Happy clients",
        "stat_experience": "Years of experience",
        "stat_support": "Ongoing support",

        # Services
        "services_title": "Our Services",
        "services_subtitle": "Complete digital marketing solutions built to grow your business",
        "services_cta": "Learn more",
        "services_all": "All services",

        # Why us / Features
        "why_title": "Why Athar Media?",
        "why_subtitle": "We combine creativity and professionalism to deliver real results",
        "feature_1_title": "Modern Designs",
        "feature_1_text": "Branding and websites with modern designs that reflect your professionalism.",
        "feature_2_title": "Real Results",
        "feature_2_text": "Well-studied ad campaigns that target your customers and actually grow sales.",
        "feature_3_title": "Local Team",
        "feature_3_text": "A Gaza-based team that understands your local market and speaks your audience's language.",
        "feature_4_title": "Ongoing Support",
        "feature_4_text": "We stay with you after delivery with continuous follow-up and technical support.",

        # Process (how we work)
        "process_title": "How we work",
        "process_sub": "Simple, clear steps from idea to launch",
        "step_1_title": "Consultation",
        "step_1_text": "We listen to your idea and understand your business, goals and target audience.",
        "step_2_title": "Planning & Design",
        "step_2_text": "We set the strategy and design the right solutions for your brand.",
        "step_3_title": "Execution",
        "step_3_text": "We build the website and launch the ad campaigns professionally.",
        "step_4_title": "Follow-up & Growth",
        "step_4_text": "We analyze results and continuously improve performance for the best ROI.",

        # Portfolio
        "portfolio_title": "Our Work",
        "portfolio_subtitle": "A selection of projects where we made a difference",
        "portfolio_view": "View project",
        "portfolio_visit": "Visit website",
        "portfolio_empty": "Projects will be added soon.",
        "filter_all": "All",
        "filter_restaurant": "Restaurants",
        "filter_clinic": "Clinics",
        "filter_store": "Stores",
        "filter_cafe": "Cafés",
        "filter_other": "Other",

        # Testimonials
        "testi_title": "What our clients say",
        "testi_subtitle": "Our clients' trust is our true impact",

        # CTA band
        "cta_band_title": "Ready to make a digital impact?",
        "cta_band_text": "Get in touch today and receive a free consultation for your project.",
        "cta_band_button": "Contact us now",

        # About page
        "about_title": "About Us",
        "about_subtitle": "Our story and mission",
        "about_intro": "Athar Media is a digital marketing agency from the heart of Gaza, specialized in website design and ad campaign management for restaurants, clinics, stores and cafés.",
        "about_story_title": "Our Story",
        "about_story_text": "We started with a simple vision: to help local businesses grow in the digital world. We believe every business deserves a digital presence worthy of it, and we work to create a real, lasting impact for our clients.",
        "mission_title": "Our Mission",
        "mission_text": "To empower businesses in Gaza to reach their customers and grow their sales through creative, professional digital solutions.",
        "vision_title": "Our Vision",
        "vision_text": "To be the leading digital partner for local businesses, creating a distinctive impact for every brand.",
        "values_title": "Our Values",
        "value_1": "Creativity",
        "value_2": "Professionalism",
        "value_3": "Commitment",
        "value_4": "Transparency",

        # Contact page
        "contact_title": "Contact Us",
        "contact_subtitle": "Tell us about your project and we'll get back to you shortly",
        "contact_info_title": "Contact Information",
        "contact_phone": "Phone",
        "contact_email": "Email",
        "contact_address": "Address",
        "contact_hours": "Working hours",
        "contact_whatsapp": "Message us on WhatsApp",
        "contact_follow": "Follow us on",
        "form_name": "Full name",
        "form_email": "Email address",
        "form_phone": "Phone number",
        "form_business": "Business type",
        "form_service": "Requested service",
        "form_service_choose": "Choose a service (optional)",
        "form_message": "Your message",
        "form_send": "Send message",
        "form_required": "This field is required",
        "form_success": "Your message has been sent successfully! We'll contact you soon.",
        "form_error": "Something went wrong, please check the fields and try again.",

        # Footer
        "footer_about": "A Gaza-based digital marketing agency. We design websites and run ad campaigns to create a lasting impact for your business.",
        "footer_links": "Quick links",
        "footer_services": "Our services",
        "footer_contact": "Contact us",
        "footer_rights": "All rights reserved",
        "footer_made": "Made with ❤ in Gaza",
        "back_home": "Back to home",
        "read_more": "Read more",
        "page_not_found": "Page not found",
    },
}


def get_ui(lang):
    """Return the UI string table for the given language (falls back to Arabic)."""
    return UI.get(lang, UI["ar"])
