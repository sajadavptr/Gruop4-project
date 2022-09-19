from pickletools import int4
from django.shortcuts import render
from mania.models import Court,Account,Booking
from django.http import HttpResponse
from mania.forms import forms
from .forms import BookingForm, bookingForm
from .forms import BookingForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def index(request):
    return render(request,"mania/login.html")


def login(request):
    return render(request, 'login.html')

def courts_view(request):
    courts = Court.objects.all()
    content = {
        "courts" : courts

    }

    return render(request,"mania/courts.html",content)


 
# Create your views here.
def bookingform_view(request):
    print(request.user.pk)
    initial_dict = {
        "account" : request.user.pk,
    }
    if request.method.lower() == "get":
        form = BookingForm(data=None, initial = initial_dict)
    else:
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.save()
    context ={"form": form}
    return render(request, "mania/bookingform.html", context)
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return render(request, 'mania/registeration.html',{})
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return render(request, "mania/registeration.html")
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('login_user')


        else:
            messages.info(request, 'Both passwords are not matching')
            return render(request, "mania/registeration.html")
            

    else:
        return render(request, "mania/registeration.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('/login')



    else:
        return render(request, '/mania/login.html')








def home(request):
    return render(request, 'mania/home.html',{})
    #return redirect('/mania/home/')

def logout_user(request):
    auth.logout(request)
    return redirect('/mania/home/')
    #return render(request,"/login.html",{})
    
