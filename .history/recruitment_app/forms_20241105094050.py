from django.forms import ModelForm

from recruitment_app.models import Applicant,Employer,Application,Jobposting,Qualification,Jobrequirements

class Applicant_form(ModelForm):
    class Meta:
        model = Applicant
        fields = '__All__'
        
class Employer_form(ModelForm):
    class Meta:
        model = Employer
        field = '__All__'
        
class Jobposting_form(ModelForm):
    class Meta:
        model = Jobposting
        field = '__All__'
    
class Qualification_form(ModelForm):
    class Meta:
        model = Qualification
        field = {'Qualification_name','Qualification_Acronym','Awarding_institution'} # use this to specify the fields to be displayed on the form   
    
class Jobrequirements_form(ModelForm):
    class Meta:
        model = Jobrequirements
        field = {'Education_level','Experience'}  
        
class Application_form(ModelForm):
    class Meta:
        model = Application
        field = {'Application_date','Application_status'} 
        
                                