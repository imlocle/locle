from django.shortcuts import render

def index (request):
    return render(request, 'website/index.html')

def finder(request):
    return render(request, 'website/finder.html')

def writenow(request):
    return render (request, 'website/writenow.html')

def guilty(request):
    return render (request, 'website/guilty.html')

# Create your views here.
