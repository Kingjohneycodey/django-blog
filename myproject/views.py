# from django.http import HttpResponse

from django.shortcuts import render

# def homepage(request):
#     return HttpResponse('Home page')

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')
