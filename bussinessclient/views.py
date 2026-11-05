from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import students,Signin

# Create your views here.
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

        return redirect('home')

    return render(request, "studentspages/add.html")


def Signpage(request):



    if request.method == "POST":
       susername = request.POST.get("susername")
       semail = request.POST.get('semail')
       spass = request.POST.get('spass')
       scpass = request.POST.get('scpass')

       Signin.objects.create(
           susername=susername,
           semail=semail,
           spass=spass,
           scpass=scpass

       )
       return redirect('students')

    Singininfo = Signin.objects.all()
     
    return render(request, 'studentspages/signin.html',{
        'signin' : Singininfo
    })


def Readloigin(request):
    Singininfo = Signin.objects.all()
    return render(request, 'studentspages/read.html',{
        'info' : Singininfo
    })




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

