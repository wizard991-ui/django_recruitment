from django.forms import Modelform

from recruitment_app.model import Applicant,Employer,Application,Jobposting,Qualification,Jobrequirements

class Applicant_form(ModelForm):
    class Meta:
        model = Applicant
        field= '__All__'
        
class Employer_form(ModelForm):
    class Meta:
        model = Employer
        field = '__All__'
        
class Jobposting_form(ModelForm):
    class = Jobposting
    field = '__All__'
    
class Qualification_form(ModelForm):
    class = Qualification
    field = {Qualification_name = models.CharField(max_length=50)
    Qualification_Acronym = models.CharField(max_length'Awarding_institution'}                    