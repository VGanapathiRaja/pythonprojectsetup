from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Index(request):
    return HttpResponse("Hello World...!!!")


def Homepage(request):
    myData = {
        "Title" :"HomePAge"
    }
    return render(request, 'index.html',myData)

def Aboutpage(request):
    return render(request,"about.html")

def Servicepage(request):
    return render(request,"service.html")

def Contactpage(request):
    return render(request,"contact.html")