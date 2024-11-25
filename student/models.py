from django.db import models

# Create your models here.
class Department(models.Model):
    student_department = models.CharField(max_length=100)

    def __str__(self)->str:
        return self.student_department
    
    class Meta:
        ordering = ['student_department']  

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self)->str:
        return self.student_id
    

class Student(models.Model):
    student_department = models.ForeignKey(Department,related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID , related_name="std_id",  on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField(default=18)
    student_email = models.EmailField(unique=True)
    student_address = models.TextField()
    

    def __str__(self):
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"
      

class Subject(models.Model):
    subject_name  = models.CharField(max_length=100)
    
    def __str__(self):
        return self.subject_name    
    

class StudentMarks(models.Model):
    student = models.ForeignKey(Student , related_name= "std_marks", on_delete= models.CASCADE)
    subject = models.ForeignKey(Subject, related_name= "subject", on_delete=models.CASCADE) 
    marks = models.IntegerField()
    
    def __str__(self):
        return f"{self.student.student_name} {self.subject.subject_name} {self.marks}"
    
    class Meta:
        unique_together = ['student','subject']
        

class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name="std_report_card", on_delete= models.CASCADE)
    student_rank = models.IntegerField()
    date_of_report_card_generation = models.DateField(auto_now_add=True)
    
    
    class Meta:
        unique_together = ["student_rank","date_of_report_card_generation"]