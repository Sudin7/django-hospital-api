from rest_framework import serializers
from employee.models import Type,Staff,Patient


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'  

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'  #staff name, department, email        

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields= '__all__'