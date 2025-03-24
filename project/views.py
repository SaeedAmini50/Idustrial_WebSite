from django.shortcuts import render
from django.http import HttpResponse

def home (requset):
    return render(requset , 'index.html')

def about (requset):
    return render(requset , 'about.html')

def blog (requset):
    return render(requset , 'blog.html')

def portfolio (requset):
    return render(requset , 'portfolio.html')

def service (requset):
    return render(requset , 'service.html')

def single (requset):
    return render(requset , 'single.html')

def cnc (requset):
    return render(requset , 'cnc.html')

def team (requset):
    return render(requset , 'team.html')

def contact (requset):
    return render(requset , 'contact.html')