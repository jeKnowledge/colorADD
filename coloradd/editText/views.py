import django
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Noticias
from .models import Clothing
from .models import Environment
from .models import Health
from .models import Transport
from .models import Game
from .models import Supplies
from .forms import HomeForm
from .models import Post
from django.core.mail import send_mail


def about_view(request):

    if request.method == "GET":
        form = HomeForm()
        return render(request,'about.html', {'form':form})
    elif request.method =="POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('tema2',str(form.cleaned_data['contract'])+"\n"+str(form.cleaned_data['name'])+"\n"+str(form.cleaned_data['email'])+"\n"+str(form.cleaned_data['subject'])+"\n"+str(form.cleaned_data['text']),'coloradd@hotmail.com',['coloradd@hotmail.com'],fail_silently=False)
    return HttpResponseRedirect("/about/")

def midia_view(request):

    if request.method == "GET":
        form = HomeForm()
        midiaText = Noticias.objects.all()
        return render(request,'midia.html',{'query':midiaText, 'form': form})
    elif request.method =="POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('tema2',str(form.cleaned_data['contract'])+"\n"+str(form.cleaned_data['name'])+"\n"+str(form.cleaned_data['email'])+"\n"+str(form.cleaned_data['subject'])+"\n"+str(form.cleaned_data['text']),'coloradd@hotmail.com',['coloradd@hotmail.com'],fail_silently=False)
    return HttpResponseRedirect("/midia/")




def index_view(request):

    if request.method == "GET":
        form = HomeForm()
        indexText = Noticias.objects.all()
        return render(request,'index.html',{'query':indexText,"form":form})
    elif request.method =="POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()

            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print("AAAAA")
            print(send_mail('tema2',str(form.cleaned_data['contract'])+"\n"+str(form.cleaned_data['name'])+"\n"+str(form.cleaned_data['email'])+"\n"+str(form.cleaned_data['subject'])+"\n"+str(form.cleaned_data['text']),'coloradd@hotmail.com',['coloradd@hotmail.com'],fail_silently=False))

    return HttpResponseRedirect("/")

def colorblindness_view(request):

    if request.method == "GET":
        form = HomeForm()
        return render(request,'colorblindness.html', {'form':form})
    elif request.method =="POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('tema2',str(form.cleaned_data['contract'])+"\n"+str(form.cleaned_data['name'])+"\n"+str(form.cleaned_data['email'])+"\n"+str(form.cleaned_data['subject'])+"\n"+str(form.cleaned_data['text']),'coloradd@hotmail.com',['coloradd@hotmail.com'],fail_silently=False)
    return HttpResponseRedirect("/colorblindness/")

def clothingView(request):
    pics = Clothing.objects.all()
    return render(request, 'solutions.html',{'query':pics})

def EnvironmentView(request):
    pics = Environment.objects.all()
    return render(request, 'solutions.html',{'query2':pics})

def HealthView(request):
    pics = Health.objects.all()
    return render(request, 'solutions.html',{'query3':pics})

def TransportView(request):
    pics = Transport.objects.all()
    return render(request, 'solutions.html',{'query4':pics})

def GameView(request):
    pics = Game.objects.all()
    return render(request, 'solutions.html',{'query5':pics})

def SuppliesView(request):
    pics = Supplies.objects.all()
    return render(request, 'solutions.html',{'query6':pics})

def code_view(request):
    if request.method == "GET":
        form = HomeForm()
        return render(request,'code.html', {'form':form})
    elif request.method =="POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('tema2',str(form.cleaned_data['contract'])+"\n"+str(form.cleaned_data['name'])+"\n"+str(form.cleaned_data['email'])+"\n"+str(form.cleaned_data['subject'])+"\n"+str(form.cleaned_data['text']),'coloradd@hotmail.com',['coloradd@hotmail.com'],fail_silently=False)
    return HttpResponseRedirect("/code/")

def solutions_view(request):
    if request.method == "GET":
        form = HomeForm()
        pics = Clothing.objects.all()
        pics2 = Environment.objects.all()
        pics3 = Health.objects.all()
        pics4 = Transport.objects.all()
        pics5 = Game.objects.all()
        pics6 = Supplies.objects.all()
        return render(request,'solutions.html', {'query':pics,'query2':pics2, 'query3':pics3,'query4':pics4,'query5':pics5,'query6':pics6, 'form':form})
    elif request.method =="POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('tema2',str(form.cleaned_data['contract'])+"\n"+str(form.cleaned_data['name'])+"\n"+str(form.cleaned_data['email'])+"\n"+str(form.cleaned_data['subject'])+"\n"+str(form.cleaned_data['text']),'coloradd@hotmail.com',['coloradd@hotmail.com'],fail_silently=False)
    return HttpResponseRedirect("/solutions/")
# Create your views here.
