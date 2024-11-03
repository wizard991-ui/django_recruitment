from django.shortcuts import render

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
