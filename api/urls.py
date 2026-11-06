from django.urls import include, path
from . import views

urlpatterns = [
    path('Staff/',views.StaffView.as_view()),
    path('Patient/',views.PatientView.as_view()),
    path('type/',views.TypeView.as_view()),
]