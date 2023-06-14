from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=100, default='Not Disclosed')
    illness_history = models.TextField(default='')
    prescriptions = models.TextField(default='')


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    doc_type = [
        ('ENT', 'ENT'),
        ('Cardiologist', 'Cardiologist'),
        ('Neurologist', 'Neurologist'),
        ('Oncologist', 'Oncologist'),
        ('Orthopedia', 'Orthopedia'),
        ('Pediatrician', 'Pediatrician')
        ]
    doctor = models.CharField(max_length=20, choices=doc_type)
    
    def __str__(self):
        return self.name


class Appointment(models.Model):
    description = models.TextField(default='')
    docs = [
        ('ENT', 'ENT'),
        ('Cardiologist', 'Cardiologist'),
        ('Neurologist', 'Neurologist'),
        ('Oncologist', 'Oncologist'),
        ('Orthopedia', 'Orthopedia'),
        ('Pediatrician', 'Pediatrician')
        ]
    doc_type = models.CharField(max_length=20, choices=docs)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)
    complaints = models.TextField(default='')
    
    def __str__(self):
        return f'{self.user.username} Appointment'


class Approved_Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.appointment.user.username} Approved Appointment'


class Billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()
    status = models.BooleanField(default=False)

    