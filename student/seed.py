import random
from .models import *
from faker import Faker
faker = Faker()

def create_subject_marks():
    try:
        students = Student.objects.all()
        for student in students:
            subjects = Subject.objects.all()
            for subject in subjects:
                StudentMarks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(0,100)
                )
        
    except Exception as e :
        print(e)

def seed_db(n=10)->None:
    try:  
        for i in range(0,n):
            department_objs = Department.objects.all()
            random_index = random.randint(0, len(department_objs)-1)
            student_department = department_objs[random_index]
            student_id = f"STD-CS-{random.randint(100,9999)}"
            student_name = faker.name()
            student_age = random.randint(10,100)
            student_email = faker.email()
            student_address = faker.address()  
            student_id_obj = StudentID.objects.create(student_id= student_id)
            
            student_obj = Student.objects.create(
                student_department = student_department,
                student_id = student_id_obj,
                student_name = student_name,
                student_age = student_age,
                student_email = student_email,
                student_address = student_address
            )
    except Exception as e:
        print(e)