PR Assistant — Standard Edition

نسخهٔ Standard از PR Assistant — یک ابزار سبک برای تحلیل خودکار Pull Requestها و گذاشتن کامنت‌های فوری برای تیم‌های کوچک و فریلنسرها.

قابلیت‌ها (Standard)

دریافت webhook از GitHub (PR created / synchronized)

آنالیز سریع diff (قواعد اولیه: TODO, debug prints, large files)

ارسال کامنت ساختاریافته به PR

Dockerized و اجرا با یک دستور

خروجی گزارش JSON / CSV

.env.example برای تنظیمات

3 روز پشتیبانی ایمیلی

نصب (Docker)

.env را از .env.example بساز و متغیرها را پر کن (GITHUB_APP_ID, GITHUB_PRIVATE_KEY یا GITHUB_TOKEN)

ساخت و اجرا:

docker-compose up -d --build


بررسی لاگ‌ها:

docker-compose logs -f web

Local Dev (بدون Docker)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# ویرایش .env و سپس
uvicorn app.main:app --reload --port 8000

استفاده با GitHub

ساخت GitHub App یا استفاده از GitHub Actions wrapper

webhook را به https://your-host/webhook تنظیم کنید

پشتیبانی و تحویل

تحویل: ZIP شامل سورس، Dockerfile، README، demo GIF

پشتیبانی: 3 روز ایمیلی. درخواست نصب جداگانه (upsell).

License

Proprietary — see LICENSE.txt

Contact

برای خرید و نصب و پشتیبانی: godcraft1380@gmail.com