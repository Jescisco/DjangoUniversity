from django.db import models
from django.core.validators import *

class Teachers(models.Model):
    name = models.CharField(max_length=75, verbose_name='Name')
    last_name = models.CharField(max_length=75, verbose_name='Last Name')
    tag = models.CharField(
        max_length=4,
        validators=[RegexValidator(r'^[0-9]+$')],
        verbose_name='Tag')
    phone_number = models.CharField(
        max_length=7,
        validators=[RegexValidator(r'^[0-9]+$')],
        verbose_name="Phone Number",
    )
    email = models.EmailField(max_length=80, verbose_name='Email')
    genre = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        ],
        verbose_name='Genre'
    )
    birthdate = models.DateField(verbose_name='Birthdate')

class SchoolSubjects(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    credits_units = models.IntegerField(
        validators=[MaxValueValidator(2)],
        verbose_name='Credit Units'
    )
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
