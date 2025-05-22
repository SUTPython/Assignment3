+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

----------
![توضیح تصویر](https://s6.uupload.ir/files/screenshot_2025-05-06_211714_ihhy.png)

سال ۲۰۲۵ است. شما به‌عنوان یک برنامه‌نویس تازه‌کار در استودیوی **Warner Bros** مشغول به کار شده‌اید. مدیر بخش آرشیو با عجله به شما مراجعه می‌کند:

"فردا بیست و پنجمین سالگرد پخش قسمت آخر سریال **Friends** است و ما می‌خواهیم برای طرفداران یک گزارش آماری از دیالوگ‌های شخصیت‌های اصلی تهیه کنیم. متأسفانه برنامه‌نویس اصلی امروز حضور ندارد و ما به کمک شما نیاز داریم!"

## وظیفه شما

شما باید یک تابع به نام **analyze_friends_script** بنویسید که:

1. یک مسیر فایل را به عنوان ورودی دریافت کند که شامل دیالوگ‌های سریال است.

2.  فایل را بخواند و تحلیل کند.

3.  تعداد دیالوگ‌های هر شخصیت را بشمارد.

4.  تعداد خنده‌ها (هر جایی که عبارت **"(laugh)"** در دیالوگ آمده) برای هر شخصیت را محاسبه کند.

5.  طولانی‌ترین دیالوگ هر شخصیت را مشخص کند.

6.  نتایج را در قالب یک دیکشنری برگرداند.

**شما باید حتماً مدیریت خطاها را با exception handling انجام دهید.**

# ورودی
فایل متنی که هر خط آن شامل یک دیالوگ به فرمت زیر است:

شخصیت: دیالوگ

مثال محتوای فایل:

Ross: We were on a break!

Joey: How you doin'? (laugh)

Chandler: Could I BE any more sarcastic?

Monica: I know!

Rachel: Oh my God!

Phoebe: Oh, no no no!

Ross: I'm fine. (laugh)
# خروجی
یک دیکشنری که کلیدهای آن نام شخصیت‌ها هستند و مقادیر آن دیکشنری‌هایی شامل اطلاعات زیر:

+ **"dialogue_count"**: تعداد دیالوگ‌های آن شخصیت

+ **"laugh_count"**: تعداد دیالوگ‌هایی که شامل خنده هستند

+ **"longest_dialogue"**: طول طولانی‌ترین دیالوگ آن شخصیت

همچنین، یک کلید اضافی به نام "total" که شامل اطلاعات کلی است:

+ **"total_dialogues"**: کل تعداد دیالوگ‌ها

+ **"total_characters"**: تعداد شخصیت‌های منحصربفرد

+ **"total_laughs"**: تعداد کل خنده‌ها


## نکات مهم

1.  از try-except برای مدیریت خطاهای احتمالی استفاده کنید.

2.  دقیقاً استثناهای زیر را مدیریت کنید:

+ ارور FileNotFoundError: وقتی که فایل وجود نداشته باشد **("Error: The specified file was not found")**

+ استثنای عمومی Exception برای سایر خطاهای پیش‌بینی نشده **("Error: {error message}")**

4.  در صورتی که فایل خالی باشد یا هیچ دیالوگی نداشته باشد، پیام **("Error: The file is empty or contains no dialogue")**

5.  خطوط خالی یا فقط شامل فضای خالی را نادیده بگیرید.

# مثال

## ورودی نمونه ۱

با فرض اینکه محتوای فایل friends_script.txt به شکل زیر باشد:
```
Ross: We were on a break!

Joey: How you doin'? (laugh)

Chandler: Could I BE any more sarcastic?

Ross: I'm fine. (laugh)

```


## خروجی نمونه 1
```
{

	"Ross": {

		"dialogue_count": 2,

		"laugh_count": 1,

		"longest_dialogue": 19  # طول "We were on a break!"

	},

	"Joey": {

		"dialogue_count": 1,

		"laugh_count": 1,

		"longest_dialogue": 14  # طول "How you doin'?"

	},

	"Chandler": {

		"dialogue_count": 1,

		"laugh_count": 0,

		"longest_dialogue": 30  # طول "Could I BE any more sarcastic?"

	},

	"total": {

		"total_dialogues": 4,

		"total_characters": 3,

		"total_laughs": 2

	}

}
```
