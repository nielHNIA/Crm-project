from django.shortcuts import render
from .models import *
# Create your views here.
def project(request):
    return render(request, 'project_management/project.html')



def project_detail(request):
    return render(request, 'project_management/project_detail.html')


def client(request):
    return render(request, 'project_management/client.html')


def clients(request):
    return render(request, 'project_management/clients.html')



def contractors(request):
    return render(request, 'project_management/contractors.html')



def contractor(request):
    return render(request, 'project_management/contractor.html')


def sites(request):
    return render(request, 'project_management/sites.html')


def site(request):
    return render(request, 'project_management/site.html')


def teams(request):
    return render(request, 'project_management/teams.html')

def team(request):
    return render(request, 'project_management/team.html')



def reports(request):
    return render(request, 'project_management/reports.html')


def report(request):
    return render(request, 'project_management/report.html')
