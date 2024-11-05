from django.forms import Modelform

from recruitment_app.model import Applicant,Employer,Application,Jobposting,Qualification,Jobrequirements

class Applicant_form(ModelForm):
    class Meta:
        model = Applicant
        field= '__All__'
        