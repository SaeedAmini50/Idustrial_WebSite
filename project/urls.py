from django.urls import path
from project.views import home,about,blog,portfolio,service,team,contact,cnc,header,footer,single,number2


app_name = 'project'
urlpatterns = [
    
    path('', home , name='home'),
    path('about/', about , name='about'),
    path('blog/', blog , name='blog'),
    path('portfolio/', portfolio , name='portfolio'),
    path('service/', service , name='service'),
    path('single/', single , name='single'),
    path('team/', team , name='team'),
    path('contact/', contact , name='contact'),
    path('cnc/', cnc , name='cnc'),
    path('header/', header , name='header'),
    path('footer/', footer , name='footer'),
    path('number2/', number2 , name='number2'),
    

    
]