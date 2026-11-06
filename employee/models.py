from django.db import models


class Type(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name


class Staff(models.Model):
    type_name = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)
    staff_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(default='Unknown', max_length=200)
    salary = models.IntegerField(default=0)


    def __str__(self):
        return self.staff_name


class Patient(models.Model):
    patient_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=200)
    staff_name = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    date_admitted = models.DateField()

    def __str__(self):
        return self.patient_name
