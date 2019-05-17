from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.utils.translation import gettext as _
from django.utils import translation

# Create your views here.

def login_view(request):
    
    login_form = LoginForm(request.POST or None)
    registration_form = RegistrationForm(request.POST or None)
    context = {
        "login_form": login_form,
        "registration_form": registration_form
    }
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            if login_form.is_valid():
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "accounts/login.html", context)
        elif request.POST.get('submit_reg_form') == 'sign_up':
            if registration_form.is_valid():
                username = registration_form.cleaned_data["new_username"]    
                password = registration_form.cleaned_data["new_password"]
                email = registration_form.cleaned_data["email"]
                user = User.objects.create_user(username, email, password)
                user.first_name = registration_form.cleaned_data["first_name"]
                user.last_name = registration_form.cleaned_data["last_name"]
                user.save()
                reg_message = _("Account created, please login")
                return render(request, "accounts/login.html", {"reg_message": reg_message, "login_form": login_form, "registration_form": registration_form})
            else:
                return render(request, "accounts/login.html", context)
    else:
        return render(request,"accounts/login.html", context)    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))