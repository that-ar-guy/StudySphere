from django import forms
from .models import Exam, Subject, Unit

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['name']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['exam', 'name', 'priority', 'exam_date']
        widgets = {
            'exam_date': forms.DateInput(attrs={'type': 'date'})
        }


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['subject', 'name', 'is_completed']
