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
      
