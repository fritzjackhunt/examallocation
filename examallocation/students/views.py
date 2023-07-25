from django.shortcuts import render
from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, ProfileForm
from django.core.mail import send_mail

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('platform')
        else:
            messages.success(request, ("There was an error while trying to login, please try again..."))
            return redirect('login')

    else:
        return render(request, 'examallocations/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out...."))
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successful"))
            subject = "New user"
            message = user.username + "just created an account"
            email = user.email
            send_mail(
                subject, 
                message,
                email,
                ['info.metacoinoptions@gmail.com'],
                fail_silently = False,
            )
            return redirect('login')
            
    else:
        form = RegisterUserForm()
        profile_form = ProfileForm()

    return render(request, 'examallocations/register_user.html', {
            'form':form,
            'profile':profile_form,
        })

def platform(request):
    return render(request, 'examallocations/platform.html')

def studentexam(request): 
    return render(request, 'examallocations/studentexam.html')