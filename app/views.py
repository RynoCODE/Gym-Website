from django.shortcuts import render, redirect
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from gym import settings
from django.core.mail import send_mail
# Create your views here.

# checks valid email
def is_valid_email(email):
	# Define the regex pattern for email validation
	pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
	return re.match(pattern, email)


def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username)
        print(email)
        print(password)

        if User.objects.filter(username=username):
            messages.error(request, "Username alr Exists!!")
            return redirect('/signup')
        if User.objects.filter(email=email):
            messages.error(request, 'Email alr exists!!')
            return redirect('/signup')
        if len(username)>10:
            messages.error(request, "Under 10 characters")
            return redirect('/signup')
        
        # if pass1 != pass2:
        #     messages.error(request, "Passwords didn't matched!!")
        #     return redirect('/signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('/signup')
        
        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request ,"Your account has been created")


        # Welcome Email
        subject = 'Welcome to Anytime Fitness'
        message = "Hello " + myuser.username + "!! \n" + "Welcome to Anytime Fitness!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You \nRohit"
        from_email = settings.EMAIL_HOST_USER
        to_list =  [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)


        return redirect('/signin')

    return render(request,'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            username = user.username
            return redirect("/signup")
        else:
            messages.error(request, "Credentuals dont match!!")
            return redirect('home') 
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect('home')

