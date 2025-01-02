from django.urls import path
from .views import add_exam, add_subjects, add_units, welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('add-exam/', add_exam, name='add_exam'),
    path('add-subjects/<int:exam_id>/', add_subjects, name='add_subjects'),
    path('add-units/<int:subject_id>/', add_units, name='add_units'),
]
