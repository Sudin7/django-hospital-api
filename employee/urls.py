from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_patients.as_view(),name='add_patients'),
]