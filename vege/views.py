from django.shortcuts import render , redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required   
# Create your views here.
@login_required(login_url="/login/")
def recepies(request):
    # Handling form submission
    if request.method == "POST":
        data = request.POST
        recepie_name = data.get("recepie_name")
        recepie_description = data.get("recepie_description")
        recepie_image = request.FILES.get("recepie_image")
       
        # Creating a new recipe instance
        Recepie.objects.create(
            recepie_name=recepie_name,
            recepie_description=recepie_description,
            recepie_image=recepie_image
        )
        return redirect("/recepies")
    
    # Retrieving recipes, with optional search functionality
    query_set = Recepie.objects.all()
    search_query = request.GET.get("search")
    if search_query:
        query_set = query_set.filter(recepie_name__icontains=search_query)
    
    # Context for rendering
    context = { "recepies": query_set }
    
    return render(request, "recepies.html", context=context)


def delete_recepie(request,id):
    Recepie.objects.get(id=id).delete()
    return redirect("/recepies")

def update_recepie(request, id):
    try:
        recepie = Recepie.objects.get(id=id)
    except Recepie.DoesNotExist:
        return redirect("/recepies")  # Redirect if the recipe does not exist

    if request.method == "POST":
        data = request.POST
      
        recepie_name = data.get("recepie_name")
        recepie_description = data.get("recepie_description")
        recepie_image = request.FILES.get("recepie_image")

        # Update the fields if values are provided
        if recepie_name:
            recepie.recepie_name = recepie_name
        if recepie_description:
            recepie.recepie_description = recepie_description
        if recepie_image:
            recepie.recepie_image = recepie_image

        recepie.save()  # Save the updated instance
        return redirect("/recepies")

    context = { "recepie": recepie }
    return render(request, "update_recepie.html", context=context)


def login_view(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, "User does not exist!")
            return redirect("/login")

        user = authenticate(username=username, password=password) 
        if user is None:
            messages.info(request, "Invalid username or password!")
            return redirect("/login")

        # Log the user in
        login(request, user)
        messages.success(request, "Login successful!")
        return redirect("/recepies")  # Redirect to the home page or dashboard

    return render(request, "login.html")

def sign_up(request):
    if request.method == "POST":
        data= request.POST
        user = User.objects.filter(username=data.get("first_name")+ data.get("last_name"))
        if user.exists():
            messages.warning(request, "This username is already exist")
            return redirect("/sign_up")
        user =  User.objects.create(
                first_name = data.get("first_name"),
                last_name = data.get("last_name"),
                username =data.get("username")
                )
    
        user.set_password( data.get("password"))
        user.save()
        messages.success(request, "you are registerd successfully ")
        # return redirect("/sign_up")
    return render(request,"sign_up.html")

def logout_view(request):
    logout(request)
    return redirect("/login/")
