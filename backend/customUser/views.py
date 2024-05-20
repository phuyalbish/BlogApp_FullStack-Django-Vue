from django.shortcuts import render
import json
from .models import Users, AccessToken
from django.http import JsonResponse
import jwt, math, time
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def register(request):
    requestData = json.loads(request.body)
    try:
        Users.objects.values().get(email=requestData['email'])
        return JsonResponse("Email already exists", safe=False, status=400)
    except:
        Users.objects.create(email=requestData['email'], password=requestData['password'])
        user = Users.objects.values().get(email=requestData['email'])
        payload = GenerateNewToken(user.get('id'))
        response = JsonResponse(payload, safe=False, status=200)
        return response
        


def GenerateNewToken(userId):
    access_payload={
        'token_type':'access',
        'jti': math.floor(time.time()  - 100),
        'id':userId,
        'exp': math.floor(time.time() + 10000),
        'iat': math.floor(time.time()),
    }
    refresh_payload={
        'token_type':'refresh',
        'id':access_payload.get('jti'),
        'exp': math.floor(time.time() + 2592000),
        'iat': math.floor(time.time()),
    }
    payload={
        "accessJWT":jwt.encode(access_payload, "mrvishope",  algorithm="HS256"),
        "refreshJWT":jwt.encode(refresh_payload, "mrvishope",  algorithm="HS256")
    }
    newToken = AccessToken.objects.create(jti=access_payload.get('jti'), userid=access_payload.get('id'))
    newToken.save()
    return payload




def RegenerateToken(id):

    AccessTokenDB = AccessToken.objects.get(userid=id) 
    access_payload={
        'token_type':'access',
        'jti': math.floor(time.time()  - 100),
        'id':id,
        'exp': math.floor(time.time() + 10000),
        'iat': math.floor(time.time()),
    }
    refresh_payload={
        'token_type':'refresh',
        'id':access_payload.get('jti'),
        'exp': math.floor(time.time() + 2592000),
        'iat': math.floor(time.time()),
    }

    payload={
        "accessJWT":jwt.encode(access_payload, "mrvishope",  algorithm="HS256"),
        "refreshJWT":jwt.encode(refresh_payload, "mrvishope",  algorithm="HS256")
    }
     
    AccessTokenDB.jti = access_payload.get('jti')
    AccessTokenDB.save()
    return payload



def RegenerateTokenFromJTI(id):
    AccessTokenDB = AccessToken.objects.get(jti=id) 
    access_payload={
        'token_type':'access',
        'jti': math.floor(time.time()  - 100),
        'id':1,
        'exp': math.floor(time.time() + 10000),
        'iat': math.floor(time.time()),
    }
    refresh_payload={
        'token_type':'refresh',
        'id':access_payload.get('jti'),
        'exp': math.floor(time.time() + 2592000),
        'iat': math.floor(time.time()),
    }

    payload={
        "accessJWT":jwt.encode(access_payload, "mrvishope",  algorithm="HS256"),
        "refreshJWT":jwt.encode(refresh_payload, "mrvishope",  algorithm="HS256")
    }    
    AccessTokenDB.jti = access_payload.get('jti')
    AccessTokenDB.save()
    return payload


def verify(func):
    def wrapper(request, *args, **kwargs):
        if request.headers.get('Authorization'):
            try:
                payload = jwt.decode(request.headers.get('Authorization'), 'mrvishope', algorithms='HS256')
                print(request.headers.get('RefreshToken'))
                responseData = func(request, payload['id'])
                response = {
                        "status":200,
                        "resData": responseData,
                    }
            except:
                response = {
                            "status": 200,
                            "resData": "Not Authenticated",
                        }
        else:
                try:
                    payload = jwt.decode(request.headers.get('RefreshToken'), 'mrvishope', algorithms='HS256')
                    response = {    
                            "status": 204,
                            "resData": RegenerateTokenFromJTI(payload['id']),
                        }
                except:
                    response = {
                            "status": 200,
                            "resData": "No Token",
                        }
        return JsonResponse(response, safe=False, status=200)
    return wrapper




@csrf_exempt
def logins(request):
    requestData = json.loads(request.body)
    try:
        data =  Users.objects.values().get(email=requestData['email'],is_deleted=False)
        if data['password'] == requestData['password']:
            jwt = RegenerateToken(data['id'])
            allData ={
                "data": DataWithoutPass(data),
                "jwt" : jwt
            }
            response =  JsonResponse(allData, safe=False, status=200)
            # response['accessToken'] = payload.get('accessJWT')
            # response['refreshToken'] = payload.get('refreshJWT')
            return response
        else:
            return JsonResponse("Wrong UserName/Password", safe=False, status=400)
    except:
        return JsonResponse("Wrong UserName/Password", safe=False, status=400)




@csrf_exempt
@verify
def checkToken(request, id):
    try:
        data =  Users.objects.values().get(pk=id, is_deleted=False)
        print(data)
        datawithoutPass = DataWithoutPass(data)
        print(datawithoutPass)
        return datawithoutPass
    except:
        return "No Dataa"

def DataWithoutPass(data):
    datawithoutPass = {
        "id": data['id'],
        "email": data['email'],
        "fname": data['fname'],
        "bio": data['bio'],
        'gender': data['gender'],
        "img_src": data['img_src'],
        "total_follower": data['total_follower'],
        "total_post": data['total_post'],
        "link": data['link'],
    }
    return datawithoutPass





@csrf_exempt
def checkMailAvailable(request):
    datas = Users.objects.all()
    available = True
    emailId = json.loads(request.body)
    for data in datas:
        if data.email == emailId["checkEmailID"]:
            available = False
            break
    return JsonResponse({"availability": available } , safe=False, status=200)



@csrf_exempt
def getUsersData(request):
    datas = list(Users.objects.values().filter(is_deleted=False))
    datawithoutPass = []
    for data in datas:
        datawithoutPass.append({
            "id": data['id'],
            "username": data['username'],
            "fullname": data['fullname'],
            'gender': data['gender'],
            "phone": data['phone'],
            "skills": data['skills_id'],
            "field": data['field_id'],
            "faculty": data['faculty_id'],
            "interest": data['interest_id'],
            "email": data['email'],
            "country": data['country_id'],
            "city": data['city_id'],
            "link": data['link'],
        })
    return JsonResponse(datawithoutPass, safe=False, status=200)

@csrf_exempt
def setUsersData(request):
    data = json.loads(request.body)
    Users.objects.create(**data)
    return JsonResponse(data, safe=False, status=200)

@csrf_exempt
def editUserData(request, **kwargs):
    user_id = kwargs["id"]
    data = json.loads(request.body)
    updateuser = Users.objects.get(pk=user_id)
    updateuser.__dict__.update(data)
    updateuser.save()
    res = {
                "data": data,
                "message": "User Updated"
            }
    
    return JsonResponse(res, safe=False, status=200)



