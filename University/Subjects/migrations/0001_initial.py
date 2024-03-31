# Generated by Django 5.0.2 on 2024-03-02 21:41

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Name')),
                ('last_name', models.CharField(max_length=75, verbose_name='Last Name')),
                ('tag', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^[0-9]+$')], verbose_name='Tag')),
                ('phone_number', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator('^[0-9]+$')], verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=80, verbose_name='Email')),
                ('genre', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, verbose_name='Genre')),
                ('birthdate', models.DateField(verbose_name='Birthdate')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('credits_units', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2)], verbose_name='Credit Units')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subjects.teachers')),
            ],
        ),
    ]
