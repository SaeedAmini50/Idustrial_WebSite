from django.urls import path
from project.views import home


urlpatterns = [
    
    path('', home , name='home'),
]