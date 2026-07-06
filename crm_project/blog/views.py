from django.shortcuts import render

from django.shortcuts import render
from .models import Pet


from django.shortcuts import render
from .models import Pet


def home(request):

    pets = Pet.objects.all()

    return render(
        request,
        "blog/home.html",
        {
            "pets": pets
        }
    )


def about(request):

    return render(request,"blog/about.html")


def contact(request):

    return render(request,"blog/contact.html")