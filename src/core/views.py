from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models

# Create your views here.

def create_plan(request):
    if request.method == 'GET':
        return render(request, 'site/create_plan.html')

    if request.method == 'POST':
        plan = models.Plan()
        plan.plan_name = request.POST['name']
        plan.price = request.POST['price']
        plan.save()
        return redirect('create_plan')

def update_plan(request, id):
    plan = models.Plan.objects.get(id=id)
    
    if request.method == 'GET':
        return render(request, 'site/update_plan.html', context={'plan': plan})
    
    if request.method == 'POST':
        plan.plan_name = request.POST['name']
        plan.price = request.POST['price']
        plan.save()
        return redirect('update_plan', id=id)