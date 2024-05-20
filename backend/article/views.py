from django.shortcuts import render
from .models  import  Articles
from django.http import JsonResponse
import jwt, math, time
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def getAllArticle(request):
    datas = list(Articles.objects.values().filter(is_deleted=False))
    return JsonResponse(datas, safe=False, status=200)


def getArticle(request, **kwargs):
    id = kwargs["id"]
    datas = list(Articles.objects.values().filter(is_deleted=False, authorid=id))
    return JsonResponse(datas, safe=False, status=200)

@csrf_exempt
def addArticle(request):
    data = json.loads(request.body)
    Articles.objects.create(**data)
    return JsonResponse(data, safe=False, status=200)

@csrf_exempt
def editArticle(request, **kwargs):
    user_id = kwargs["id"]
    data = json.loads(request.body)
    updateuser = Articles.objects.get(pk=user_id)
    updateuser.__dict__.update(data)
    updateuser.save()
    res = {
                "data": data,
                "message": "User Updated"
            }
    
    return JsonResponse(res, safe=False, status=200)



@csrf_exempt
def deleteArticle(request, **kwargs):
    user_id = kwargs["id"]
    data = json.loads(request.body)
    updateuser = Articles.objects.get(pk=user_id)
    updateuser.is_deleted = True
    updateuser.save()
    res = {
                "data": data,
                "message": "Article Deleted"
            }
    
    return JsonResponse(res, safe=False, status=200)