from django.shortcuts import render

from recruitment_app.forms import Applicant_form, Employer_form,Jobposting_form,Qualification_form,Jobrequirements_form,Application_form

# Create your views here.
def index_view(request):
    return render(request,'index.html')

# creating Form views

def add_applicant_View(request):
    message=''
    if request.method == 'POST':
        applicant_form = Applicant_form(request.POST)
    
        if applicant_form.is_valid():
            applicant_form.save()
            message='Applicant Registered'
    else: applicant_form = Applicant_form()
    
    # Read operation code
    applicants = Applicant.objects.all()
    
    context = {'form':applicant_form,'message':message, 'applicants':}
    return render(request,'addapplicant.html',context)       

def add_employer_view(request):
    message = ''
    if request.method == 'POST':
        employer_form = Employer_form(request.POST)
        
        if employer_form.is_valid():
            employer_form.save()
            
            message = 'Employer Registered successfully'
    else: employer_form = Employer_form()
    
    context = {'form':employer_form, 'message':message}
    return render(request,'addemployer.html',context)  

def add_jobposting_view(request):
    message = ''
    if request.method == 'POST':
        jobposting_from = Jobposting_form(request.POST)
        
        if jobposting_form.is_valid():
            jobposting_form.save()
            message='Job posting Uploaded'
    else: jobposting_form = Jobposting_form()
    
    context ={'form':jobposting_form, 'message':message}
    return render(request,'addjobposting.html',context)  

def add_qualification_view(request):
    message=''
    if request.method == 'POST':
        qualification_form = Qualification_form(request.POST)
        
        if qualification_form.is_valid():
            qualification_form.save()
            message='Qualification uploaded'
    
    else: qualification_form = Qualification_form()
    
    context={'form':qualification_form, 'message':message}
    return render(request,'addqualification.html',context)    

def add_jobrequirements_view(request):
    message=''
    if request.method=='POST':
        jobrequirement_form = Jobrequirements_form(request.POST)
        
        if jobrequirement_form.is_valid():
            jobrequirement_form.save()
            message ='Job requirements uploaded'
            
    else: jobrequirement_form = Jobrequirements_form()
    
    context={'form':jobrequirement_form,'message':message}
    return render(request,'addjobrequirement.html',context)  

def add_application_view(request):
    message=''
    if request.method == 'POST':
        application_form = Application_form(request.POST)
        
        if application_form.is_valid():
            application_form.save()
            message='Application uploaded'
    
    else: application_form = Application_form()
    
    context = {'form':application_form, 'message':message}
    return render(request,'addapplication.html',context)                          