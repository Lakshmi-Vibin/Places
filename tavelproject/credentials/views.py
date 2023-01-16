from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pswd']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials!!")
            return redirect('login')

    return render(request, "Login.html")


def Register(request):
    if request.method == 'POST':
        username = request.POST['uname']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['pswd']
        cpassword = request.POST['pswd1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already Exists!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already Exists!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email,
                                                password=password)
                user.save()
                return redirect('login')
                print("USER REGISTERED!!!!")
        else:
            messages.info(request, "Password Doesn't match!!!")
            return redirect('register')
        return redirect('/')
    return render(request, "Register.html")

def Logout(request):
    auth.logout(request)
    return redirect('/')