from django.shortcuts import render

from recruitment_app.forms import Applicant_form, Employer_form,Jobposting_form,Qualification_form,Jobrequiremets_form,Application_form

# Create your views here.
def index_view(request):
    return render(request,'index.html')

def applicant_view(request):
    return render(request, 'applicant.html')

def jobposting_view(request):
    return render(request, 'jobposting.html')

def employer_view(request):
    return render(request, 'employer.html')

def application_view(request):
    return render(request,'application.html')

def qualification_view(request):
    return render(request,'qualification.html')

def jobrequirements_view(request):
    return render(request, 'jobrequirements.html')

# creating Form views

def add_applicant_View(request):
    if request.method == 'POST':
        applicant_form = Applicant
