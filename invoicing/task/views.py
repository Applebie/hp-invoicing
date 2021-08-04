from django.shortcuts import render
from django.http import JsonResponse
from . models import Task
from django.views.decorators.csrf import csrf_exempt
import json

# axios install on top of vue i.e replace fetch methods to call api on client side)  & drf (install on top of django to enhance api features) for API routes
# bootstrap to get better UI

# Create your views here.
def index(request):
    all_task = Task.objects.all().values() # task class and objects is property of pythondb 
    all_task = list(all_task)
    #return JsonResponse({'foo':all_task})
    return JsonResponse({'tasks':all_task}) # use the key tasks in vue function to display

@csrf_exempt
def create_task(request):
    json_data = json.loads(request.body) # converts string coming json to the server into python object/dict
    newtask = Task()
    newtask.text = json_data['text']
    newtask.business = json_data['business']
    newtask.address = json_data['address']
    newtask.taxid = json_data['taxid']
    newtask.save()
    # newtask.refresh_from_db()
    #return JsonResponse({'foo':all_task})
    return JsonResponse({'tasks':json_data}) # use the key tasks in vue function to display

@csrf_exempt
def update_task(request, id):
   t = Task.objects.get(pk = id)
   #json_data = json.loads(request.body)
   #t = Task()
   t.text = request.POST.get('text')
   t.business = request.POST.get('business')
   t.address = request.POST.get('address')
   t.taxid = request.POST.get('taxid')
   t.save()
   #t.refresh_from_db()
   return JsonResponse({'status':'updated'})

@csrf_exempt
def delete_task(request,id):
   # t = Task.objects.get(pk = id)
   #json_data = json.loads(request.body)
   # id = request.POST.get('id')
   print(id)
   t = Task.objects.get(pk = id)
   t.delete()
   #t.refresh_from_db()
   return JsonResponse({'status':'deleted'})