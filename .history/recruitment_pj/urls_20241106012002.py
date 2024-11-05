"""
URL configuration for recruitment_pj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recruitment_app.views import index_view,jobposting_view,add_applicant_View,add_employer_view, add_jobposting_view,add_qualification_view,add_jobrequirements_view,add_application_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index_page'),
    path('addapplicant/',add_applicant_View, name="addapplicant_page"),
    path('addemployer/',add_employer_view, name='addemployer_page'),
    path('addjobposting/',add_jobposting_view, name='addjobposting_page'),
    path('addqualification/', add_qualification_view, name='addqualification_page'),
    path('addjorequirement/',add_jobrequirements_view, name ='addrequirement_page'),
    path('addapplication/',add_application_view, name='addapplication_page')
]
