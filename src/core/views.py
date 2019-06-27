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

def list_all_plans(request):
    if request.method == 'GET':
        plans = models.Plan.objects.all()
        return render(request, 'site/list_all_plans.html', context={'plans': plans})

def update_plan(request, id):
    plan = models.Plan.objects.get(id=id)
    
    if request.method == 'GET':
        return render(request, 'site/update_plan.html', context={'plan': plan})
    
    if request.method == 'POST':
        plan.plan_name = request.POST['name']
        plan.price = request.POST['price']
        plan.save()
        return redirect('update_plan', id=id)

def delete_plan(request, id):
    if request.method == 'GET':
        plan = models.Plan.objects.get(id=id)
        plan.delete()
        return HttpResponse('Plano {} excluído.'.format(plan.plan_name))
