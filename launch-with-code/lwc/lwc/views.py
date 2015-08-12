from django.shortcuts import render

def home(request):
    context={}
    tempalte = "home.html"
    return render(request, template, context)
