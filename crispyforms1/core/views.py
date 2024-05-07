from django.shortcuts import render
from .forms import * 


def index(request):
    context={'form':UniversityForm()}
    return render (request,'index.html',context)