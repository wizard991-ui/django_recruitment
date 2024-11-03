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
from recruitment_app.views import index_view,applicant_view,jobposting_view,employer_view,jobrequirements_view, qualification_view, application_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index_page'),
    path('applicant/', applicant_view, name='applicant_page'),
    path('jobposting/', jobposting_view, name='jobposting_page'),
    path('employer/', employer_view, name='employer_page'),
    path('jobrequirements/', jobrequirements_view, name='jobrequirements_page'),
    path('application/', application_view, name ='application_page'),
    path
    
]
