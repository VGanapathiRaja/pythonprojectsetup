from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="index"),

    path('home/',views.Homepage, name="home"),
    path('about/',views.Aboutpage, name="about"),
    path('service/',views.Servicepage,name='service'),
    path('contact/',views.Contactpage,name='contact'),

   
    path('empcreatedata/',views.Empadd, name="empcreatedata"),
    path('empreaddata/',views.Emppage, name="empreaddata"),
    path('empupdatedata/<int:id>',views.Empupdate, name="empupdatedata"),
    path('empdeletedata/<int:id>',views.EmpDelete, name="empdeletedata"),

    
    path('students/',views.Studentspage,name='students'),
    path('studesreaddata/',views.Studnetsread,name="studnetsreaddata"),
    path('studnetsupdate/<int:id>/',views.studnetsUpdate,name="studnetsupdate"),
    path('studnetsdeletedata/<int:id>/',views.studnetsDelete,name="studnetsdeletedata"),

    path('signin/', views.Signpage, name="signin"),
    path('readinfo/', views.Readloigin, name="readinfo"),
    path('updatedata/<int:id>/', views.Signinupdate, name="updatedata"),
    path('deletedata/<int:id>/', views.Signdelte, name="deletedata"),






      
]