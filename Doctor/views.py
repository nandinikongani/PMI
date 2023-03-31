from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from Doctor.models import doctorModel,doctorreportmodel
from Doctor.forms import doctorForm
from forensic.models import *
from forensic.forms import *
import speech_recognition as sr
import pyttsx3


def index(request):
    return render(request,'index.html')


def doctorlogin(request):
    return render(request,'doctor/doctorlogin.html')

def doctorregister(request):
        if request.method == 'POST':
            form1 = doctorForm(request.POST)
            if form1.is_valid():
                form1.save()
                print("succesfully saved the data")
                return render(request, 'doctor/doctorlogin.html')
                # return HttpResponse("registreration succesfully completed")
            else:
                print("form not valied")
                return HttpResponse("form not valied")
        else:
            form = doctorForm()
            return render(request, "doctor/doctorregister.html", {"form": form})

def doctorlogincheck(request):
    if request.method == 'POST':
        sname = request.POST.get('email')
        print(sname)
        spasswd = request.POST.get('upasswd')
        print(spasswd)
        try:
            check = doctorModel.objects.get(email=sname,passwd=spasswd)
            # print('usid',usid,'pswd',pswd)
            print(check)
            request.session['name'] = check.name
            print("name",check.name)
            status = check.status
            print('status',status)
            if status == "Activated":
                request.session['email'] = check.email
                return render(request, 'doctor/doctorpage.html')
            else:
                messages.success(request, 'doctor is not activated')
                return render(request, 'doctor/doctorlogin.html')
        except Exception as e:
            print('Exception is ',str(e))
            pass
        messages.success(request,'Invalid name and password')
        return render(request,'doctor/doctorlogin.html')

def bodydetails1(request):
    qs=bodydetails.objects.all()
    return render(request,'doctor/bodydetails1.html',{"object":qs})


def doctorreport(request):
    return render(request,'doctor/doctorreport.html')


def doctorreport1(request):
    bid=request.POST.get('t1')
    qs=bodydetails.objects.filter(bid=bid)
    print("qs:",qs)
    return render(request,'doctor/doctorreport1.html',{"object":qs})



def doctorfinalreport(request):
    r = sr.Recognizer()
    print("r:", r)

    # Function to convert text to
    # speech
    def SpeakText(command):

        # Initialize the engine
        engine = pyttsx3.init()
        print("engine:", engine)
        engine.say(command)
        print("hello:", engine.say(command))
        engine.runAndWait()
        print(engine.runAndWait())

    # Loop infinitely for user to
    # speak

    SpeakText("report submitted")
    if request.method == 'POST':
        name1=request.POST.get('t1')
        print("name",name1)
        bid=request.POST.get('bid')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        ldh=request.POST.get('ldh')
        print("ldh",type(ldh))
        ast=request.POST.get('ast')
        print("ast",type(ast))
        triglycerides=request.POST.get('triglycerides')
        phlevel=request.POST.get('phlevel')
        rpt=int(ast)+int(triglycerides)+int(ldh)
        print("rpt:",type(rpt))
        phlevel=int(phlevel)

        if rpt<=500 and phlevel==7:
            pmi='24hrs'
        elif rpt>=550 and phlevel<7 and phlevel>=5:
            pmi='48hrs'
        elif rpt>=550 and phlevel<5 and phlevel>=4:
            pmi='72hrs'
        else:
            pmi='more than 72hrs'
        pmi=str(pmi)
        print(type(pmi))
        ldh=str(ldh)
        ast=str(ast)
        triglycerides=str(triglycerides)
        doctorreportmodel.objects.create(name=name1,bid=bid,age=age,gender=gender,ldh=ldh,ast=ast,triglycerides=triglycerides, phlevel=phlevel,pmi=pmi)
        return render(request, 'doctor/doctorreport1.html')












