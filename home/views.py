from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):

    if request.method == 'POST':
        return HttpResponse('This is the home page with a POST')
    else:
        return HttpResponse(request.method)