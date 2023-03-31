from django.shortcuts import render
from django.http import  HttpResponse
from Doctor.models import doctorModel,doctorreportmodel
from forensic.models import *

def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname =='admin' and passwd =='admin':
            return render(request,"admin/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")
    return render(request, "admin/adminloginentered.html")


def doctordetails(request):
    qs=doctorModel.objects.all()
    return render(request,'admin/doctordetails.html',{"object":qs})

def logout(request):
    return render(request,"index.html")

def activatedoctor(request):
    if request.method == 'GET':
        uname = request.GET.get('pid')
        print(uname)
        status = 'Activated'
        print("pid=", uname, "status=", status)
        doctorModel.objects.filter(id=uname).update(status=status)
        qs = doctorModel.objects.all()
        return render(request,"admin/doctordetails.html", {"object": qs})


def finalreport(request):
    qs=doctorreportmodel.objects.all()
    return render(request,'admin/finalreport.html',{"object":qs})


def adminbodydetails(request):
    qs = bodydetails.objects.all()
    return render(request, 'admin/adminbodydetails.html',{"object": qs})






