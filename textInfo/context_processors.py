from .models import Number, TextEntry, HeaderInfo

def numbers_processor(request):
    """
    این پردازشگر زمینه، چهار عدد اول را از مدل Number به تمام قالب‌ها ارسال می‌کند.
    """
    numbers = Number.objects.all()[:4]  # فقط 4 عدد اول
    return {
        'numbers': numbers
    }

def header_info_processor(request):
    """
    این پردازشگر زمینه، اطلاعات هدر را به تمام قالب‌ها ارسال می‌کند.
    """
    try:
        header_info = HeaderInfo.objects.first()
    except HeaderInfo.DoesNotExist:
        header_info = None
    
    return {
        'header_info': header_info
    }
