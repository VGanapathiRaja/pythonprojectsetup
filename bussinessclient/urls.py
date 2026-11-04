from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="index"),

    path('home/',views.Homepage, name="home"),
    path('about/',views.Aboutpage, name="about"),
    path('service/',views.Servicepage,name='service'),
    path('contact/',views.Contactpage,name='contact'),
    path('students/',views.Studentspage,name='students'),
      
]