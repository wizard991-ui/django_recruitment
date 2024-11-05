from django.forms import ModelForm

from recruitment_app.models import Applicant,Employer,Application,Jobposting,Qualification,Jobrequirements

class Applicant_form(ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__',
        
class Employer_form(ModelForm):
    class Meta:
        model = Employer
        fields = '__All__'
        
class Jobposting_form(ModelForm):
    class Meta:
        model = Jobposting
        fields = '__All__'
    
class Qualification_form(ModelForm):
    class Meta:
        model = Qualification
        fields = {'Qualification_name','Qualification_Acronym','Awarding_institution'} # use this to specify the fields to be displayed on the form   
    
class Jobrequirements_form(ModelForm):
    class Meta:
        model = Jobrequirements
        fields = {'Education_level','Experience'}  
        
class Application_form(ModelForm):
    class Meta:
        model = Application
        fields = {'Application_date','Application_status'} 
        
                                