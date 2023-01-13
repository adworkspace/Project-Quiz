from django.shortcuts import render
from django.http import HttpResponse
from Point.models import Question,Category

# Create your views here.
def index(request):
    allques=Question.objects.all()
    context={"questions":allques}
    return render(request,"Point/home.html",context)

def about(request):
    return render(request,'Point/about.html')

def contact(request):
    return render(request,'Point/contact.html')
    
def login(request):
    return render(request,'Point/login.html')

def signup(request):
    return render(request,'Point/signup.html')