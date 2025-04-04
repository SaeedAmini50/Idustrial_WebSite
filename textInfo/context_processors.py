from .models import Number, TextEntry

def numbers_processor(request):
    """
    این پردازشگر زمینه، چهار عدد اول را از مدل Number به تمام قالب‌ها ارسال می‌کند.
    """
    numbers = Number.objects.all()[:4]  # فقط 4 عدد اول
    return {
        'numbers': numbers
    }
