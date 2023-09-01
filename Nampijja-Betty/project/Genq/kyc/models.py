from django.db import models
from django.core.validators import RegexValidator
import datetime
from django.core.exceptions import ValidationError

# Create your models here.
# class User(models.Model):
#     name =models.CharField(max_length=50,null=False,)
name_validator = RegexValidator(r'^[A-Za-z-]+$', 'Only alphabetic characters and hyphens are allowed.')

def validate_min_length(value):
    if len(value) < 2:
        raise ValidationError("Field must have at least 2 characters.")

def validate_age(birth_date):
    age = datetime.date.today() - birth_date
    age = int(age.days / 365.25) # approximate
    if age < 18:
        raise ValidationError("Minimum age is 18.")


class Register(models.Model):
    first_Name = models.CharField(max_length=255,null=False,blank=False, validators=[name_validator,validate_min_length])
    last_Name = models.CharField(max_length=255,null=False,blank=False, validators=[name_validator,validate_min_length])
    date_of_birth =models.DateField( validators=[validate_age])
    address = models.CharField(max_length=255,null=False,blank=False,validators=[validate_min_length])
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country =models.CharField(default='Uganda',max_length=20,null=False,blank=False)
    state =models.CharField(default='State',max_length=20,null=False,blank=False)
    Town =models.CharField(default='Town',max_length=20,null=False,blank=False)
    Zip_code =models.CharField(default=000,max_length=20,null=False,blank=False)
    phone =models.CharField(default='+256',max_length=30,null=False,blank=False)
    email = models.EmailField(default='@example.com',max_length=30,null=False,blank=False)