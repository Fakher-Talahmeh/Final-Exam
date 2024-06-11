from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    locations = Location.objects.all()
    return render(request,'main.html',{"locations":locations})

def create(request):
    form = LocationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')

    else:
        form = LocationForm()
    return render(request,'create.html',{'form':form})

def update(request,pk):
    location = Location.objects.get(id=pk)
    form = LocationForm(request.POST,instance=location)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = LocationForm(instance=location)
    return render(request,'update.html',{'form':form})

def delete(request,pk):
    location = Location.objects.get(id=pk)
    return render(request,'delete.html',{'location':location})

def delete_location(request,pk):
    Location.objects.get(id=pk).delete()
    return redirect('/')