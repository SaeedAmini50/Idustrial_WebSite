from django.shortcuts import render
from django.http import HttpResponse
from textInfo.models import TextEntry, Number

def home (requset):
    return render(requset , 'index.html')


def footer (requset):
    return render(requset , 'footer.html')



def header (requset):
    return render(requset , 'header.html')





def about (requset):
    return render(requset , 'about.html')

def blog (requset):
    return render(requset , 'blog.html')

def portfolio (requset):
    return render(requset , 'portfolio.html')

def service (requset):
    return render(requset , 'service.html')

def cnc (requset):
    return render(requset , 'cnc.html')

def team (requset):
    return render(requset , 'team.html')

def contact (requset):
    return render(requset , 'contact.html')

def single(request):
    texts = TextEntry.objects.filter(is_visible=True).order_by('unique_id')
    numbers = Number.objects.all()
    return render(request, 'single.html', {'texts': texts, 'numbers': numbers})

def number2(request):
    numbers = Number.objects.all()[:4]
    return render(request, 'number2.html', {'numbers': numbers})

def home_view(request):
    return render(request, 'single.html')

def text_list_view(request):
    texts = TextEntry.objects.filter(is_visible=True).order_by('unique_id')
    return render(request, 'text_list.html', {'texts': texts})
