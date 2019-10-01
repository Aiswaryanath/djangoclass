from django.db import models

# Create your models here.
GENDER_CHOICE=(
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHERS')
)
class Students(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=10)
    address=models.TextField()
    gender=models.CharField(max_length=1,choices=GENDER_CHOICE,default='M')
    course=models.CharField(max_length=50)
class Faculty(models.Model):
         name=models.CharField(max_length=10)
         fno=models.CharField(max_length=5)
         salary=models.CharField(max_length=10)
         designation=models.CharField(max_length=15)