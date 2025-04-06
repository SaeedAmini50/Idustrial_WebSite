from .models import Number, TextEntry, HeaderInfo, FooterInfo, CompanyInfo

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

def footer_info_processor(request):
    """
    این پردازشگر زمینه، اطلاعات فوتر را به تمام قالب‌ها ارسال می‌کند.
    """
    try:
        footer_info = FooterInfo.objects.first()
    except FooterInfo.DoesNotExist:
        footer_info = None
    
    return {
        'footer_info': footer_info
    }

def company_info_processor(request):
    """
    این پردازشگر زمینه، اطلاعات معرفی شرکت را به تمام قالب‌ها ارسال می‌کند.
    """
    try:
        company_info = CompanyInfo.objects.first()
    except CompanyInfo.DoesNotExist:
        company_info = None
    
    return {
        'company_info': company_info
    }
