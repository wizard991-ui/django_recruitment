from django.contrib import admin
from .models import Applicant,Employer,Jobposting

class recruitment_appAdmin(admin.ModelAdmin):
    list_display=('Name','Date_Of_Birth','Gender','Nationality','Telephone')
    
class recruitment_appEmployer(admin.ModelAdmin):
    list_display=('Employer_name','Employer_Email','Employer_Telephone','Contact_person','PO_Box','Plot_Number','Street','City','Country')   
    
class recruitment_appJobposting(admin.ModelAdmin):
    list_display=('Position_Title','Department','Vacancies_Available','Posting_Date','Application_Deadline') 
      

# Register your models here.
admin.site.register(Applicant,recruitment_appAdmin)
admin.site.register(Employer,recruitment_appEmployer)
admin.site.register(Jobposting,recruitment_appJobposting)

