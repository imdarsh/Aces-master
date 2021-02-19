from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages

def setexam(request):
    if request.method == "POST":
        year = request.POST['year']
        semester = request.POST['semester']
        subject = request.POST['subject']
    return render(request,'sub/ffem.html',{'year':year,'semester':semester,'subject':subject})

def ffem(request):
    if request.method == "POST":
        year = request.GET['year']
        semester = request.GET['semester']
        subject = request.GET['subject'] 
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        answer = request.POST['answer']
        category = request.POST['category']
        fa = questions(year=year,semester=semester,subject=subject,question=question,option1=option1,option2=option2,option3=option3,option4=option4,answer=answer,category=category)
        fa.save()
    return render(request,'sub/ffem.html',{'year':year,'semester':semester,'subject':subject})


def exam(request):
    a = questions.objects.order_by().values('subject','year','semester').distinct()
    return render(request,'student/exam.html',{'a':a})

def start_exam(request,subject):
    que = questions.objects.filter(subject=subject)
    return render(request,'student/start_exam.html',{'que':que})