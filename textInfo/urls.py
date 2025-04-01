from django.urls import path
from . import views

app_name = 'textInfo'

urlpatterns = [
    path('texts/', views.PublicTextListView.as_view(), name='text_list'),
    path('admin/texts/', views.AdminTextListView.as_view(), name='admin_text_list'),
    path('single/', views.single, name='single'),
] 
 