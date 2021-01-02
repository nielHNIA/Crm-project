from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'common/index.html')

@login_required
def home(request):
    return render(request, 'common/home.html')

@login_required
def view_profile(request):
    return render(request, 'common/profile.html')


def top_bar(request):
    return render(request, 'common/top_bar.html')

def sidebar(request):
    return render(request, 'common/sidebar.html')
