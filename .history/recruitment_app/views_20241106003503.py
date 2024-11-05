from django.shortcuts import render

from recruitment_app.forms import Applicant_form, Employer_form,Jobposting_form,Qualification_form,Jobrequirements_form,Application_form

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
        applicant_form = Applicant_form(request.POST)
    
        if applicant_form.is_valid():
            applicant_form.save()
    else: applicant_form = Applicant_form()
    
    context = {'form':applicant_form,}
    return render(request,'addapplicant.html',context)       

def add_employer_view(request):
    if request.method == 'POST':
        employer_form = Employer_form(request.POST)
        
        if employer_form.is_valid():
            employer_from.save()
    else: employer_form = Employer_form()
    
    context = {'form':employer_form,}
    return render(request,'addemployer.html',context)  

def add_jobposting_view(request):
    if request.method == 'POST':
        jobposting_from = Jobposting_form(request.POST)
        
        if jobposting_form.is_valid():
            jobposting_form.save()
    else: jobposting_form = Jobposting_form()
    
    context ={'form':jobposting_form,}
    return render(request,'addjobposting.html',context)  

def add_qualification_view(request):
    if request.method == 'POST':
        qualification_form = Qualification_form(request.POST)
        
        if qualification_form.is_valid():
            qualification_form.save()
    
    else: qualification_form = Qualification_form()
    
    context={'form':qualification_form,}
    return render(request,'addqualification.html',context)    

def add_jobrequirements_view(request):
    if request.method=='POST':
        jobrequirement_form = Jobrequirement_form(request.POST)
        
        if jobrequirement_form.is_valid():
            jobrequirement_form.save()
            
    else: jobrequirement_form = Jobrequirement_form()
    
    context={'form':requirement_form,}
    return render(request)
    
    
                         
