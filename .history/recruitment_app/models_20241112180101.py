from django.db import models

# Create your models here.
class Applicant(models.Model):
    GENDER_OPTIONS=[('M','Male'),('F','Female')]
    
    Name = models.CharField(max_length=50)
    Date_Of_Birth = models.DateField(auto_now=False)
    Gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)
    Nationality = models.CharField(max_length=50,null=True,blank=True,default="N/A")
    Telephone = models.CharField(max_length=15)
    
class Employer(models.Model):
    Employer_name = models.CharField(max_length=50)
    Employer_Email = models.EmailField()
    Employer_Telephone = models.CharField(max_length=15)
    Contact_person = models.CharField(max_length=25)
    PO_Box = models.CharField(max_length=10000, null=True)
    Plot_Number = models.IntegerField(null=True, blank=True)
    Street = models.CharField(max_length=50)
    City = models.CharField(max_length=25)
    Country = models.CharField(max_length=20)
def __str__(self):
    return self.city    
    
class Jobposting(models.Model):
    Position_Title = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Vacancies_Available = models.IntegerField()
    Posting_Date = models.DateField(auto_now=False)
    Application_Deadline = models.DateField(auto_now=False)
def __str_(self):
    return self.city    
    
class Qualification(models.Model):
    Applicant_ID = models.ForeignKey(Applicant,on_delete = models.CASCADE)
    Qualification_name = models.CharField(max_length=50)
    Qualification_Acronym = models.CharField(max_length=10)
    Awarding_institution = models.CharField(max_length=50)  
def __str__(self):
    return self.Applicant_ID
    
class Jobrequirements(models.Model):
    Position_id = models.ForeignKey(Jobposting, on_delete = models.CASCADE) 
    Employer_id = models.ForeignKey(Employer, on_delete = models.CASCADE)
    Education_level = models.CharField(max_length=30)
    Experience = models.CharField(max_length=50) 
def __str__(self):
    return self.Employer_id    
    
class Application(models.Model):  
    Applicant_id = models.ForeignKey(Applicant,on_delete = models.CASCADE)
    Position_id = models.ForeignKey(Jobposting, on_delete = models.CASCADE)       
    Application_date = models.DateField(auto_now=False)
    Application_status = models.CharField(max_length=20)
def __str__(self):
    return self.Applicant_id``     
    
    def __str__(self):
        self.Applicant_id, Position_id     
    
    
