from django.forms import ModelForm

from recruitment_app.models import Applicant,Employer,Application,Jobposting,Qualification,Jobrequirements,

class Applicant_form(ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
        
class Employer_form(ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
        
class Jobposting_form(ModelForm):
    class Meta:
        model = Jobposting
        fields = '__all__'
    
class Qualification_form(ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__' # use this to specify the fields to be displayed on the form   
    
class Jobrequirements_form(ModelForm):
    class Meta:
        model = Jobrequirements
        fields = '__all__'  
        
class Application_form(ModelForm):
    class Meta:
        model = Application
        fields = '__all__' 
        
                                