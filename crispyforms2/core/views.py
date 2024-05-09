from django.shortcuts import render
from .forms import * 
from django.http import HttpResponse

def index(request):
    if request.method=='GET':
        context={'form':UniversityForm()}
        return render (request,'index.html',context)
    
    elif request.method=='POST':
        form=UniversityForm(request.POST)
        if form.is_valid():
            user=form.save()
            return HttpResponse('hi')
        context={'form':form}
        return render (request,'index.html',context)
            