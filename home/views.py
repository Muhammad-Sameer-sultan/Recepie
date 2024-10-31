from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
      peoples = [
        {
            "name": "Alice",
            "age": 10
        },
        {
            "name": "Bob",
            "age": 22
        },
        {
            "name": "Charlie",
            "age": 17
        },
        {
            "name": "Diana",
            "age": 21
        }
    ]
      fruits= ["tomato","apple","mango","graps"]
      text= """my text abcd"""
      return render(request , "index.html" , context={"page":"Home" ,"peoples":peoples ,"text":text , "fruits":fruits})
 

def about(request):
   context ={"page":"About"}
   return render(request , "about.html" , context)

def contact(request):
   context ={"page":"Contact"}
   return render(request , "contact.html",context)