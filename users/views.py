from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import SignUpForm


def register(request):
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('common:home')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if form.is_valid():
            login(request, user)
            redirect('common:home')
    else:
        note = "Ivalid Username or Password"
        redirect('users:login')
    return render(request, 'registeration/login.html', {note:'note'})
