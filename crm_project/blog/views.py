from django.shortcuts import render

def home(request):

    context = {

        "name":"Om",

        "city":"Mumbai",

        "is_logged_in":True,

        "pets":[
            "Dog",
            "Cat",
            "Rabbit"
        ]

    }

    return render(request,"blog/home.html",context)


def about(request):

    return render(request,"blog/about.html")


def contact(request):

    return render(request,"blog/contact.html")