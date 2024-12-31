from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam, Subject, Unit
from .forms import ExamForm, SubjectForm, UnitForm


def welcome(request):
    exams = Exam.objects.prefetch_related('subjects__units').all()
    return render(request, 'planner/welcome.html', {'exams': exams})


def add_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            return redirect('add_subjects', exam_id=exam.id)  # Redirect to add subjects
    else:
        form = ExamForm()
    return render(request, 'planner/add_exam.html', {'form': form})


def add_subjects(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.exam = exam  # Assign the subject to the correct exam
            subject.save()
            return redirect('add_units', subject_id=subject.id)  # Redirect to add units
    else:
        form = SubjectForm()
    return render(request, 'planner/add_subjects.html', {'form': form, 'exam': exam})


def add_units(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.subject = subject  # Assign the unit to the correct subject
            unit.save()
            return redirect('welcome')  # Redirect back to the welcome page
    else:
        form = UnitForm()
    return render(request, 'planner/add_units.html', {'form': form, 'subject': subject})
