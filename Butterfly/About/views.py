from django.shortcuts import render

# Create your views here.

def aboutPage(request):
    return render(request, "About/index1.html")
