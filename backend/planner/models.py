from django.db import models

# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=100)  # Exam name (e.g., Midterms, Finals)
    date = models.DateField()  # Overall exam date

    def __str__(self):
        return self.name


class Subject(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100)  # Subject name
    priority = models.IntegerField()  # Subject priority (e.g., 1 = High, 2 = Medium, etc.)
    exam_date = models.DateField()  # Subject-specific exam date

    def __str__(self):
        return f"{self.name} (Priority: {self.priority})"


class Unit(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='units')
    name = models.CharField(max_length=100)  # Unit name
    is_completed = models.BooleanField(default=False)  # Completion status for tracking progress

    def __str__(self):
        return f"{self.name} ({'Completed' if self.is_completed else 'Pending'})"
