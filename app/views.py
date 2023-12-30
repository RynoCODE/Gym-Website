from django.shortcuts import render, redirect
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from gym import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from . tokens import generate_token
from django.core.mail import EmailMessage
import razorpay
from django.contrib.auth.decorators import login_required


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
        myuser.is_active=False
        myuser.save()
        messages.success(request ,"Your account has been created")


        # Welcome Email
        subject = 'Welcome to Anytime Fitness'
        message = "Hello " + myuser.username + "!! \n" + "Welcome to Anytime Fitness!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You \nRohit"
        from_email = settings.EMAIL_HOST_USER
        to_list =  [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)


        #Email Address confirmation
        current_site = get_current_site(request)
        email_subject = "Confirmation for Email Registration @ Anytime Fitness"
        message2 = render_to_string('email_confirmation.html',{
            'name': myuser.username,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser),
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()



        return redirect('/signin')

    return render(request,'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active == True:

                login(request, user)
                username = user.username
                return redirect("price")
        else:
            messages.error(request, "Credentuals dont match!!")
            return redirect('/signin') 
    return render(request,'signin.html')

@login_required
def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect('home')

def activate(request, uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')
    

@login_required
def price(request):
    if request.method == 'POST':
        if request.POST.get(''):
            pass
        client = razorpay.Client(auth=(settings.AUTH, settings.KEY))

        DATA = {
            "amount": 100,
            "currency": "INR",
            "receipt": "receipt#1",
            "notes": {
                "key1": "value3",   
                "key2": "value2"
            }
        }
        payment = client.order.create(data=DATA)
    return render(request, "pricing.html")
