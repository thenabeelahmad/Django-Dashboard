from os import error
# from django.db.models.expressions import Random
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import User
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import login as auth_login
from accounts.models import User,userdevices
from getmac import get_mac_address as gma
import random
import socket
import subprocess
# to get system informations
import wmi
c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]
# Create your views here.

def login(request):
    #Check if the user is logged in
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        # if user authentication success
        
        if user is not None:
            auth_login(request, user)
            # checking for same device login or new device
            try:
                if User.objects.filter(userdeviceaddress = gma(),username=username).count() == 0:
                    # will look what could be done
                    pass
                else:
                    # will send mail to user to alert for new device login 
                    pass
            except error:
                print(error)       
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, "accounts/login.html", {
                "message": "Invalid username and/or password"
            })
    return render(request, "accounts/login.html")

def signup(request):
    #Check if the user is logged in
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    if request.method == "POST":
        username = request.POST["email"].lower()
        fulln = request.POST['fulname']
        password = request.POST["passwrd"]
        email = request.POST["email"]
        phn = request.POST["phone"]
        confirmation = request.POST["cpass"]
        # check for valid mobile number
        if len(phn)!=10:
            return render(request, "accounts/signup.html", {
                "message": "Please enter a valid 10 digit number, ( Avoid +91 )."
            })
        #check if the password is the same as confirmation
        if len(password)<8:
            return render(request, "accounts/signup.html", {
                "message": "Password must be of 8 letters."
            })
        # check for password match 
        if password != confirmation:
            return render(request, "accounts/signup.html", {
                "message": "Passwords must match."
            })
        #Checks if the username is already in use
        if User.objects.filter(email = email).count() == 1:
            return render(request, "accounts/signup.html", {
                "message": "Email already taken."
            })
        try:
            # user = User.objects.create_user(username = username, password = password, email = email,first_name=fulln)
            # user.save()
            a = User()
            a.username=username
            a.userkeyid=f'{chr(random.randrange(65,90))}{chr(random.randrange(65,90))}{random.randrange(999999999999)}'
            a.userpassword=password
            a.useremail=email
            a.userfirstname=fulln
            a.userphone=phn
            a.useraccountstatus=1
            a.userdeviceaddress=gma()
            a.username=username
            a.userdeviceaddress=gma()
            a.useripaddress = socket.gethostbyname(socket.gethostname())
            a.usersystemfullinfo = subprocess.check_output("ipconfig").decode('utf-8')
            a.usermanufacturer=my_system.Manufacturer
            a.usermodel=my_system.Model
            a.userpcfamily=my_system.SystemFamily
            a.userpctype=my_system.SystemType
            a.userpcname=my_system.Name
            a.save()
            auth_login(request,a)
            return HttpResponseRedirect(reverse('signup'))
        except IntegrityError:
            return render(request, "accounts/signup.html", {
                "message": "Username already taken"
            })
    return render(request, "accounts/signup.html")


def lout(request):
  logout(request)
  return HttpResponseRedirect(reverse('login'))