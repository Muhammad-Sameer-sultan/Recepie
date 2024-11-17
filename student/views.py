from django.shortcuts import render
from .models import *

# Create your views here.

def get_students(request):
    query_set = Student.objects.all()
    
    return render(request, "student.html" , {'query-set': query_set} )
