from django.shortcuts import render
from employee.forms import PatientForm
from employee.models import Patient
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse_lazy

class add_patients(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = Patient
    template_name = 'add_patients.html'
    context_object_name = 'patients'
    form_class = PatientForm
    success_url = reverse_lazy('home')   #after adding it goes to url"home"
    permission_required = 'employee.add_patient' #appname.action_modelname