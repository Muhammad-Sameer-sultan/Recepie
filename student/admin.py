from django.contrib import admin
from .models import *
from django.db.models import Q ,Sum

# Register your models here.
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

class StudentMarkAdmin(admin.ModelAdmin):
    list_display = ['student' , 'subject' , 'marks' ]
    
admin.site.register(StudentMarks, StudentMarkAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student' , 'student_rank' , 'total_marks' , 'date_of_report_card_generation' ]
    ordering = ["student_rank"]
    
    def total_marks(self, obj):
        subject_marks = StudentMarks.objects.filter(student = obj.student)
        total_marks = subject_marks.aggregate(marks = Sum("marks"))['marks']
        return total_marks
        
    
admin.site.register(ReportCard, ReportCardAdmin)
