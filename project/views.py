from django.shortcuts import render
from django.http import HttpResponse

def home (requset):
    return render(requset , 'index.html')