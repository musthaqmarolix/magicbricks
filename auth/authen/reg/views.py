from django.shortcuts import render

# Create your views here.
def HomePage(request):
    pass
    # return render(request,'home.html')

def SignupPage(request):
    return render(request,'signup.html')

def LoginPage(request):
    pass
    # return render(request,'login.html')