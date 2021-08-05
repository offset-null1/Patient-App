from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Gender(models.TextChoices):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=Gender.choices)
    age =  models.PositiveIntegerField(null=True, blank=True)
    disease = models.CharField(max_length=50)
    doctor_name = models.CharField(max_length=50)
    fees = models.PositiveIntegerField(default=500)
    started_med_on_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"\nFirst Name: {self.first_name}\n Last Name: {self.last_name}\n Gender: {self.gender}\n Age: {self.age}\n Disease: {self.disease}\n Doctor's Name: {self.doctor_name}\n Fees: {self.fees}\n Medication start date: {self.started_med_on_date}\n"