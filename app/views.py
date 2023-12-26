from django.shortcuts import render
import re
# Create your views here.

# checks valid email
def is_valid_email(email):
	# Define the regex pattern for email validation
	pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
	return re.match(pattern, email)


def home(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def signin(request):
     return render(request, 'signin.html')