from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import *

def home(request):
    subjects_list = SchoolSubjects.objects.order_by('id')
    paginator = Paginator(subjects_list, 2)
    page_number = request.GET.get('page') or 1
    subjects = paginator.get_page(page_number)

    return render(request, 'home.html', {'subjects':subjects})

def teachers(request):
    teachers = Teachers.objects.all()

    pagination = Paginator(teachers, 10)

    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)

    return render(request, "teachers.html", {"teachers":teachers})

def add_teacher(request):
    name = request.POST['name']
    last_name = request.POST['last_name']
    tag = request.POST['tag']
    phone_number = request.POST['phone_number']
    email = request.POST['email']
    genre = request.POST['genre']
    birthdate = request.POST['birthdate']

    Teachers.objects.create(name=name, last_name=last_name, tag=tag, phone_number=phone_number, email=email, genre=genre, birthdate=birthdate)

    return redirect('/teachers')

def edit_teacher(request, id):
    teacher = Teachers.objects.get(id=id)
    return render(request, 'teachers-edit.html', {"teacher":teacher})

def update_teacher(request):
    id = request.POST['id']
    name = request.POST['name']
    last_name = request.POST['last_name']
    tag = request.POST['tag']
    phone_number = request.POST['phone_number']
    email = request.POST['email']
    genre = request.POST['genre']
    birthdate = request.POST['birthdate']

    teacher = Teachers.objects.get(id=id)
    teacher.name = name
    teacher.last_name = last_name
    teacher.tag = tag
    teacher.phone_number = phone_number
    teacher.email = email
    teacher.genre = genre
    teacher.birthdate = birthdate

    teacher.save()

    return redirect('/teachers')

def delete_teacher(request, id):
    teacher = Teachers.objects.get(id=id)
    teacher.delete()

    return redirect('/teachers')

def school_subjects(request):
    school_subjects = SchoolSubjects.objects.all()
    teachers = Teachers.objects.all()

    return render(request, 'school-subjects.html', {'school_subjects':school_subjects, 'teachers':teachers})

def add_school_subject(request):
    name = request.POST['name']
    credits_units = request.POST['credits_units']
    teacher_id = request.POST['teacher']

    SchoolSubjects.objects.create(name=name, credits_units=credits_units, teacher_id=teacher_id)

    return redirect('/schoolSubjects')

def edit_school_subject(request, id):
    school_subject = SchoolSubjects.objects.get(id=id)
    teachers = Teachers.objects.all()
    return render(request, 'school-subjects-edit.html', {"school_subject":school_subject, 'teachers':teachers})

def update_school_subject(request):
    id = request.POST['id']
    name = request.POST['name']
    credits_units = request.POST['credits_units']
    teacher_id = request.POST['teacher']

    school_subject = SchoolSubjects.objects.get(id=id)
    school_subject.name = name
    school_subject.credits_units = credits_units
    school_subject.teacher_id = teacher_id

    school_subject.save()

    return redirect('/schoolSubjects')

def delete_school_subject(request, id):
    school_subject = SchoolSubjects.objects.get(id=id)
    school_subject.delete()

    return redirect('/schoolSubjects')
