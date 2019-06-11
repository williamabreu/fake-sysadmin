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