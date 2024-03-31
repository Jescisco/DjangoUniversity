from django.urls import path
from Subjects.views import *

urlpatterns = [
    path('', home),
    path('teachers/', teachers),
    path('addTeacher/', add_teacher),
    path('editTeacher/<int:id>/', edit_teacher),
    path('updateTeacher/', update_teacher),
    path('deleteTeacher/<int:id>/', delete_teacher),
    path('schoolSubjects/', school_subjects),
    path('addSchoolSubject/', add_school_subject),
    path('editSchoolSubject/<int:id>/', edit_school_subject),
    path('updateSchoolSubject/', update_school_subject),
    path('deleteSchoolSubject/<int:id>/', delete_school_subject)
]
