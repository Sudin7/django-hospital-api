from django.shortcuts import render

from employee.models import Patient
from django.views.generic import ListView


class home(ListView):
    model = Patient
    template_name = 'home.html'
    context_object_name='patients'