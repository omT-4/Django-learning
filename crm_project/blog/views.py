from django.shortcuts import render

def home(request):

    context = {
        "name": "Om",
        "is_logged_in": True,
        "fruits": [
            "Apple",
            "Banana",
            "Mango"
        ]
    }

    return render(request, "blog/home.html")