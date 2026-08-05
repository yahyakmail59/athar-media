# 🚀 نشر موقع أثر ميديا على PythonAnywhere (مجاناً)

دليل النشر النهائي — مضبوط على الإعدادات الفعلية للمشروع.

| العنصر | القيمة |
|---|---|
| مستودع GitHub | `https://github.com/yahyakmail59/athar-media.git` |
| مستخدم PythonAnywhere | `AtharMedia1` |
| رابط الموقع | `https://atharmedia1.pythonanywhere.com` |
| البيئة الافتراضية | `atharenv` (Python 3.10) |
| مجلد المشروع على الخادم | `/home/AtharMedia1/athar-media` |

> 🔴 **تنبيه مهم:** لينكس يفرّق بين الأحرف الكبيرة والصغيرة في المسارات. اكتب `AtharMedia1` **بنفس الأحرف تماماً** في كل مكان. (رابط النطاق نفسه يُكتب بأحرف صغيرة: `atharmedia1`.)
>
> إن كان اسم مستخدمك مختلفاً، استبدل `AtharMedia1` في كل الأسطر بالاسم الصحيح — للتأكد شغّل `echo $HOME` في الـ Console.

---

## الجزء 1 — رفع المشروع على GitHub ✅ (تم)

الكود مرفوع بالفعل على: `https://github.com/yahyakmail59/athar-media.git`

> لرفع تعديلات جديدة لاحقاً من جهازك:
> ```bash
> git add -A
> git commit -m "تحديث"
> git push
> ```

---

## الجزء 2 — النشر على PythonAnywhere

### 1) أنشئ حساباً مجانياً
سجّل في **https://www.pythonanywhere.com/registration/register/beginner/** واختر الخطة المجانية **Beginner** (بلا بطاقة بنكية)، وسجّل الدخول.

### 2) ارفع المشروع (تبويب Consoles → Bash)
الصق هذه الأوامر دفعة واحدة وانتظر انتهاءها:

```bash
cd ~
git clone https://github.com/yahyakmail59/athar-media.git
cd athar-media
mkvirtualenv --python=/usr/bin/python3.10 atharenv
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py seed_data
python manage.py createsuperuser
```

> - آخر أمر (`createsuperuser`) سيطلب اسم مستخدم (`admin`) وبريداً وكلمة مرور — احفظها.
> - إن ظهر `atharenv already exists` فالبيئة جاهزة — اكتب `workon atharenv` وتابع بقية الأوامر.

للتأكد من المسار الصحيح، شغّل:
```bash
echo $HOME/athar-media
```
👉 يجب أن يطبع `/home/AtharMedia1/athar-media` — استخدمه **بالضبط** كما ظهر في الخطوات التالية.

### 3) أنشئ تطبيق الويب (تبويب Web)
**Add a new web app** → **Next** → اختر **Manual configuration** ⚠️ (وليس Django) → **Python 3.10** → **Next**.

### 4) اضبط المسارات (قسم Code)
| الحقل | القيمة |
|---|---|
| **Source code** | `/home/AtharMedia1/athar-media` |
| **Working directory** | `/home/AtharMedia1/athar-media` |

**قسم Virtualenv:** اكتب `atharenv` (سيكمل المسار تلقائياً `/home/AtharMedia1/.virtualenvs/atharenv`).

### 5) عدّل ملف WSGI
اضغط رابط ملف الـ WSGI (`/var/www/atharmedia1_pythonanywhere_com_wsgi.py`)، **امسح كل محتواه**، والصق:

```python
import os
import sys

path = '/home/AtharMedia1/athar-media'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'athar_media.settings'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_SECRET_KEY'] = 'GTbTALZL41TlKxbbyMyvfOiNUw_24bW9CuUJBS112KG86j1xGfGsSMpO1EKKp3Y9LAIaIOeCsoCxHLhd'
os.environ['DJANGO_ALLOWED_HOSTS'] = 'atharmedia1.pythonanywhere.com'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
ثم اضغط **Save**.

### 6) اضبط الملفات الثابتة (قسم Static files)
أضف صفّين:

| URL | Directory |
|---|---|
| `/static/` | `/home/AtharMedia1/athar-media/staticfiles` |
| `/media/`  | `/home/AtharMedia1/athar-media/media` |

### 7) شغّل الموقع 🎉
اصعد لأعلى الصفحة واضغط الزر الأخضر **Reload atharmedia1.pythonanywhere.com**، ثم افتح:

### 👉 https://atharmedia1.pythonanywhere.com
لوحة التحكم: **https://atharmedia1.pythonanywhere.com/admin/**

---

## 🩹 حل المشكلات الشائعة

- **"This directory does not exist" في حقل Source code:**
  المشروع لم يُستنسخ بعد على هذا الحساب، أو الأحرف غير مطابقة. شغّل أوامر الجزء 2/الخطوة 2 أولاً، ثم استخدم ناتج `echo $HOME/athar-media` حرفياً.
- **صفحة خطأ بعد Reload:** في تبويب **Web** افتح رابط **Error log** واقرأ آخر الأسطر — غالباً خطأ مسار أو مفتاح سري.
- **التصميم (CSS) لا يظهر:** تأكد من تشغيل `collectstatic` ومن صحة مسار `/static/` في قسم Static files، ثم اضغط Reload.
- **`DisallowedHost`:** تأكد أن `DJANGO_ALLOWED_HOSTS` في ملف WSGI = `atharmedia1.pythonanywhere.com`.

---

## 🔄 تحديث الموقع لاحقاً
كلما عدّلت الكود محلياً ورفعته بـ `git push`، نفّذ في Bash console على PythonAnywhere:

```bash
cd ~/athar-media
git pull
workon atharenv
python manage.py migrate
python manage.py collectstatic --noinput
```
ثم اضغط **Reload** من تبويب Web.

---

## 📝 ملاحظات
- الحساب المجاني لا "ينام"، لكنه يُعطّل إن لم تسجّل الدخول 3 أشهر — يكفي تسجيل الدخول لتجديده.
- الصور المرفوعة من لوحة التحكم تُحفظ في مجلد `media` على الخادم (لا تُرفع إلى GitHub).
- **غيّر كلمة مرور المدير** بعد أول دخول: من `/admin/` أو عبر `python manage.py changepassword admin`.
- لإضافة نطاق مخصّص لاحقاً (مثل `atharmedia.com`): يتطلب خطة مدفوعة على PythonAnywhere + شراء النطاق.
