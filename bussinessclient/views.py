from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import students

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

def Studentspage(request):
    if request.method == "POST" :
        sname = request.POST.get('sname')
        semail = request.POST.get('semail')
        smobile = request.POST.get('smobile')
        sage = request.POST.get('sage')

        students.objects.create(
            sname=sname,
            semail=semail,
            smobile=smobile,
            sage=sage
        )

        return redirect('Homepage')

    return render(request, "studentspages/add.html")