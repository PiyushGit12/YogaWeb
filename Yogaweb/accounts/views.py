from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="user_login")
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():  # Automatically call the clean_confirm_password from our Forms.py
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])  # set the password for new user
            new_user.save()
            # return HttpResponse(" User is created succesfully ")
            return redirect('user_login')
    else:  # get request
        form = UserRegistrationForm()
    return render(request, 'registrations/signup.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('blog_post_ui'))
                else:
                    return HttpResponse("User is not Active")
            else:
                return HttpResponse("Please Login With Valid Username and Password")
    else:
        form = LoginForm()
    context = {'form': form}

    return render(request, 'registrations/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('user_login')
