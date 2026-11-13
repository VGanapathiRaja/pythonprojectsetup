from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . models import students,Signin,Empinfo

# Create your views here.

def Empadd(request):
    if request.method == "POST" :
        empusername = request.POST.get('empusername')
        empuserfull = request.POST.get('empuserfull')
        empemail = request.POST.get('empemail')
        empmobile = request.POST.get('empmobile')
        empids = request.POST.get('empids')

        Empinfo.objects.create(
            empusername = empusername,
            empuserfull =empuserfull,
            empemail = empemail,
            empmobile = empmobile,
            empids = empids
        )
        return redirect('empreaddata')
    
    return render(request, "employees/createemp.html")

def Emppage(request):
    Emps = Empinfo.objects.all()
    return render(request,"employees/readeemp.html",{
        'empdetails' : Emps 
    })

def Empupdate(request,id):
    Empupdate = get_object_or_404(Empinfo,id=id)

    if request.method == "POST" :
        Empupdate.empusername = request.POST.get('empusername')
        Empupdate.empuserfull = request.POST.get('empuserfull')
        Empupdate.empemail = request.POST.get('empemail')
        Empupdate.empmobile = request.POST.get('empmobile')
        Empupdate.empids = request.POST.get('empids')

        Empupdate.save()

        return redirect('empreaddata')

    return render(request, 'employees/updateemp.html',{
        "Empupdate" : Empupdate
    })


def EmpDelete(request,id):
    Empdelete = get_object_or_404(Empinfo,id=id)
    Empdelete.delete()
    return redirect('empreaddata')




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

    studnetsReaddata = students.objects.all()

    return render(request, "studentspages/add.html",{
        'Datas' : studnetsReaddata
    })

def Studnetsread(request):
    studnetsReaddata = students.objects.all()
    return render(request, 'studentspages/add.html',{
        'Datas' : studnetsReaddata
    })

def studnetsUpdate(request,id):
    studeentUpdate = get_object_or_404(students,id=id)
    if request.method == "POST":
        studeentUpdate.sname = request.POST.get("sname")
        studeentUpdate.semail = request.POST.get("semail")
        studeentUpdate.smobile = request.POST.get('smobile')
        studeentUpdate.sage = request.POST.get('sage')

        studeentUpdate.save()

        return redirect("students")
    
    return render(request,'studentspages/updatestudents.html',{
        'updatedata' : studeentUpdate
    })


def studnetsDelete(request,id):
    studentsDelete =get_object_or_404(students,id=id)
    studentsDelete.delete()
    return redirect("students")







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
       return redirect('signin')

    Singininfo = Signin.objects.all()
     
    return render(request, 'studentspages/signin.html',{
        'signin' : Singininfo
    })


def Signinupdate(request,id):
        
        updateData = get_object_or_404(Signin, id=id)
        if request.method == "POST":
            updateData.susername = request.POST.get("susername")
            updateData.semail = request.POST.get('semail')
            updateData.spass = request.POST.get('spass')
            updateData.scpass = request.POST.get('scpass')

            updateData.save()

            return redirect("signin")

        return render(request, 'studentspages/update.html',{
        'updateData' : updateData
    })


def Signdelte(request,id):
    deleteData = get_object_or_404(Signin,id=id)
    deleteData.delete()
    return redirect('signin')



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

