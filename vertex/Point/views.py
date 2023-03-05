from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Point.models import Question,Category

# Create your views here.
def index(request):
    allcat=Category.objects.all()
    context={"categories":allcat}
    return render(request,"Point/home.html",context)

def about(request):
    return render(request,'Point/about.html')

def contact(request):
    return render(request,'Point/contact.html')

def cat(request):
    allcat=Category.objects.all()
    context={"categories":allcat}
    return render(request,'Point/category.html',context)   

def viewCat(request,cat):
    obj=Category.objects.filter(cat=cat).first()
    return render(request,'Point/viewCat.html',{'obj':obj})

def quiz(request,cat):
    print(cat)
    oobj=Category.objects.filter(cat=cat).first()
    print(oobj)
    questions=oobj.get_questions()
    context={'data':questions}  
    return render(request,'Point/quiz.html',context)
def score(request):
    if request.method=='POST':
        ans=request.POST.get('{{question.q_no}}')
        print(ans)
    return render(request,'Point/score.html')

def login(request):
    return render(request,'Point/login.html')

def signup(request):
    return render(request,'Point/signup.html')