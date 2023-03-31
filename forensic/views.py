from django.shortcuts import render
from django.http import HttpResponse
from forensic.forms import *
from Doctor.models import *
import speech_recognition as sr
import pyttsx3

def frnsclogin(request):
    return render(request, "frnsc/frnsclogin.html")



def frnscloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname =='frnsc' and passwd =='frnsc':
            return render(request,"frnsc/frnscloginentered.html")
        else:
            return HttpResponse("invalied credentials")
    return render(request, "frnsc/frnscloginentered.html")




def bodydetails(request):
        if request.method == 'POST':
            form =bodydetailsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'frnsc/bodydetails.html')
        else:
            form =bodydetailsForm()
        return render(request, 'frnsc/bodydetails.html', {'form': form})


def forensicreport(request):
    return render(request, 'frnsc/frnscreportid.html')

def frnscreport1(request):
    if request.method == 'POST':
        bid=request.POST.get('t1')
        qs=doctorreportmodel.objects.filter(bid=bid)
        for x in qs:
            pmi=x.pmi
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

        return render(request,'frnsc/finalreport1.html',{"object":qs})



















