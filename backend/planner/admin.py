from django.contrib import admin
from .models import Exam, Subject, Unit

class UnitInline(admin.TabularInline):
    model = Unit
    extra = 1  # Show one extra blank field for new Unit entries


class SubjectAdmin(admin.ModelAdmin):
    inlines = [UnitInline]  # Allows adding Units directly within the Subject admin
    list_display = ('name', 'priority', 'exam_date', 'exam')  # Display relevant fields


class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')  # Display relevant fields


admin.site.register(Exam, ExamAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Unit)
