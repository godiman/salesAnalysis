from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from account.forms import RegistrationForm, LoginForm

# Create your views here.

def registration_view(request):
    
    context = {}
    
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('login')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


# Login view
def login_view(request):
    
    context = {}
    
    user = request.user
    if user.is_authenticated:
        return redirect("home")    
    
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect("home")
    else:
        # print("InValid data")
        # print(request.POST)
        form = LoginForm()
       
    context['login_form'] = form
    return render(request, 'account/login.html', context)


# logout view
def logout_view(request):
    logout(request)
    return redirect('login')
