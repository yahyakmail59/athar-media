# 🚀 نشر موقع أثر ميديا على PythonAnywhere (مجاناً)

دليل خطوة بخطوة لرفع الموقع عبر **GitHub** ثم **PythonAnywhere**.
ستحصل على رابط مجاني مثل: `https://USERNAME.pythonanywhere.com`

> استبدل في كل الأوامر: `USERNAME` باسم مستخدمك، و`REPO` باسم المستودع (مثلاً `athar-media`).

---

## الجزء 1 — رفع المشروع على GitHub

### أ) أنشئ مستودعاً جديداً
1. ادخل إلى **https://github.com/new**
2. اسم المستودع: `athar-media` — اجعله **Private** أو **Public** كما تحب.
3. **لا** تضف README أو .gitignore (موجودان لدينا) → اضغط **Create repository**.
4. انسخ رابط المستودع، مثل: `https://github.com/USERNAME/athar-media.git`

### ب) ارفع الكود (من مجلد المشروع على جهازك)
الأوامر التالية جُهّز المستودع المحلي مسبقاً (git init + commit). نفّذ فقط:

```bash
git remote add origin https://github.com/USERNAME/athar-media.git
git branch -M main
git push -u origin main
```

> عند أول `push` سيطلب منك Git تسجيل الدخول إلى GitHub عبر المتصفح — أكمِل الدخول.

---

## الجزء 2 — النشر على PythonAnywhere

### 1) أنشئ حساباً مجانياً
سجّل في **https://www.pythonanywhere.com** واختر الخطة المجانية **Beginner** (بلا بطاقة بنكية).

### 2) استنسخ المشروع
من تبويب **Consoles** → افتح **Bash console** ونفّذ:

```bash
git clone https://github.com/USERNAME/athar-media.git
```

### 3) أنشئ بيئة افتراضية وثبّت المتطلبات

```bash
cd athar-media
mkvirtualenv --python=/usr/bin/python3.10 atharenv
pip install -r requirements.txt
```

### 4) جهّز قاعدة البيانات والملفات

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py seed_data
python manage.py createsuperuser
```

> احفظ اسم المستخدم وكلمة المرور التي ستدخلها لإنشاء حساب المدير.

### 5) ولّد مفتاحاً سرياً قوياً (احتفظ به للخطوة 7)

```bash
python -c "import secrets; print(secrets.token_urlsafe(60))"
```

### 6) أنشئ تطبيق الويب
من تبويب **Web** → **Add a new web app** → **Next** →
اختر **Manual configuration** (ليس Django) → **Python 3.10** → **Next**.

ثم في صفحة إعدادات الويب اضبط:

- **Virtualenv**: اكتب `atharenv` (سيكمل المسار `/home/USERNAME/.virtualenvs/atharenv`).
- **Source code**: `/home/USERNAME/athar-media`
- **Static files** (اضغط Enter a URL / Enter a path لكل سطر):

  | URL | Directory |
  |---|---|
  | `/static/` | `/home/USERNAME/athar-media/staticfiles` |
  | `/media/`  | `/home/USERNAME/athar-media/media` |

### 7) عدّل ملف WSGI
في صفحة **Web** اضغط على رابط ملف **WSGI configuration file**، **احذف كل محتواه** واستبدله بالتالي (مع تعديل `USERNAME` والمفتاح السري ورابط النطاق):

```python
import os
import sys

path = '/home/USERNAME/athar-media'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'athar_media.settings'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_SECRET_KEY'] = 'ضع-المفتاح-السري-الذي-ولّدته-هنا'
os.environ['DJANGO_ALLOWED_HOSTS'] = 'USERNAME.pythonanywhere.com'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

احفظ الملف (**Save**).

### 8) شغّل الموقع
ارجع لتبويب **Web** واضغط الزر الأخضر **Reload**.
افتح: **https://USERNAME.pythonanywhere.com** 🎉

---

## 🔄 تحديث الموقع لاحقاً
كلما عدّلت الكود محلياً ورفعته (`git push`)، نفّذ في Bash console على PythonAnywhere:

```bash
cd athar-media
git pull
python manage.py migrate
python manage.py collectstatic --noinput
```

ثم اضغط **Reload** من تبويب Web.

---

## 📝 ملاحظات
- الحساب المجاني لا "ينام"، لكنه ينتهي إن لم تسجّل الدخول لمدة 3 أشهر — يكفي تسجيل الدخول لتجديده.
- لوحة التحكم: `https://USERNAME.pythonanywhere.com/admin/`
- لإضافة نطاق مخصّص (مثل `atharmedia.com`) لاحقاً: تحتاج خطة مدفوعة على PythonAnywhere + شراء النطاق.
- الصور المرفوعة من لوحة التحكم تبقى محفوظة في مجلد `media` على الخادم.
```
