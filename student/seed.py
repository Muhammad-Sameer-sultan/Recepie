import random
from .models import *
from django.db.models import Q ,Sum
from django.db import transaction
from django.utils.timezone import now
from datetime import date
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
        
def create_report_card():
    # Fetch students with total marks calculated
    ranks = Student.objects.annotate(marks=Sum('std_marks__marks')).order_by('-marks', '-student_age')

    # Initialize rank counter
    rank_counter = 1
    today = date.today()

    # Use a transaction to ensure atomicity
    with transaction.atomic():
        # Create report cards in bulk
        report_cards = []
        for student in ranks:
            # Check for an existing report card to prevent duplicate creation
            if not ReportCard.objects.filter(
                student=student, date_of_report_card_generation=today
            ).exists():
                report_cards.append(
                    ReportCard(
                        student=student,
                        student_rank=rank_counter,
                        date_of_report_card_generation=today,
                    )
                )
                rank_counter += 1

        # Bulk create all report cards
        ReportCard.objects.bulk_create(report_cards)

    print(f"{len(report_cards)} report cards created successfully.")