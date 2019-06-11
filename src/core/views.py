from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'site/index.html')
    if request.method == 'POST':
        plan = models.Plan()
        plan.plan_name = request.POST['name']
        plan.price = request.POST['price']
        plan.save()
        return HttpResponse('ok!')