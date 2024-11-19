from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def get_students(request):  
    query_set = Student.objects.all()
    if  request.GET.get("search"):
        search  = request.GET.get("search")
        query_set = query_set.filter(Q(student_name__icontains = search) |Q(student_age__icontains = search) | Q(student_email__icontains = search) |Q(student_department__student_department__icontains = search)|Q(student_id__student_id__icontains = search)) 
    paginator = Paginator(query_set,10)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request, "student.html" , {'queryset': page_obj} )

def student_marks(request,student_id):
    query_set = StudentMarks.objects.filter(student__student_id__student_id = student_id)
  
    
    return render(request , "student_marks.html", {'query_set':query_set})