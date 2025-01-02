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



# Add Subjects to an Exam
def add_subjects(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        exam_date = request.POST.get('exam_date')
        Subject.objects.create(exam=exam, name=name, priority=priority, exam_date=exam_date)
        return redirect('add_subjects', exam_id=exam_id)  # Redirect to the same page to add more subjects
    subjects = exam.subjects.all()  # Fetch all subjects for this exam
    return render(request, 'planner/add_subjects.html', {'exam': exam, 'subjects': subjects})

# Example of add_units function
def add_units(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        is_completed = request.POST.get('is_completed') == 'on'
        Unit.objects.create(subject=subject, name=name, is_completed=is_completed)
        return redirect('add_units', subject_id=subject_id)
    units = subject.units.all()
    return render(request, 'planner/add_units.html', {'subject': subject, 'units': units})
