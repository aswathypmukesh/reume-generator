from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            obj = Student.objects.all().order_by('-id').first()   
            return redirect('profile',obj.id)
    if request.method == 'GET':
        form = StudentForm()
    c = {
        'form': form,
    }
    return render(request, 'home.html',c)

def profile(request, pk):
  
    if request.method == 'GET':
        std = Student.objects.get(id=pk)
        c = {
            'std': std,
        }
        return render(request, 'resume.html',c)
    