from django.shortcuts import render
from django.http import JsonResponse
from . models import Task
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def index(request):
    all_task = Task.objects.all().values() # task class and objects is property of pythondb 
    all_task = list(all_task)
    #return JsonResponse({'foo':all_task})
    return JsonResponse({'tasks':all_task}) # use the key tasks in vue function to display

@csrf_exempt
def create_task(request):
    json_data = json.loads(request.body)
    newtask = Task()
    newtask.text = json_data['text']
    newtask.business = json_data['business']
    newtask.address = json_data['address']
    newtask.taxid = json_data['taxid']
    newtask.save()
    newtask.refresh_from_db()
    #return JsonResponse({'foo':all_task})
    return JsonResponse({'tasks':json_data}) # use the key tasks in vue function to display