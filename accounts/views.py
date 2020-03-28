from django.shortcuts import render
from main.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from main.models import user
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/base.html')

def clist(request):
    return render(request, 'accounts/clist.html')

def rtask(request):
    return render(request, 'accounts/rtask.html')

def atask(request):
    return render(request, 'accounts/atask.html')

def user(request):
    return render(request, 'accounts/user.html')

def items(request):
    return render(request, 'accounts/items.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def department(request):
    return render(request, 'accounts/department.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            prof = user()
            prof.firstname = user_form.cleaned_data["firstname"]
            prof.lastname = user_form.cleaned_data["lastname"]
            prof.skills = user_form.cleaned_data["skills"]
            prof.city = user_form.cleaned_data["city"]
            prof.country = user_form.cleaned_data["country"]
            prof.email = user_form.cleaned_data["email"]
            prof.save()
            return HttpResponse("Registration Done")
    else:
        user_form = UserRegistrationForm()
    context = {
        'user_form': user_form
    }
    return render(request,
                  'accounts/register.html',
                  context=context
                  )