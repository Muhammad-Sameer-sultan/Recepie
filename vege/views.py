from django.shortcuts import render , redirect
from .models import *

# Create your views here.
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
