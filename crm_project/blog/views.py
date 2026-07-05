from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    context = {
        "name" : "om",
        "Age" : 21,
        "College": "D.G. Ruparel College of Arts, Science and Commerce"
    }
    return render(request, "blog/home.html", context)