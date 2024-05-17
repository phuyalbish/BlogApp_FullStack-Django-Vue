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
        return JsonResponse("Email already exists", safe=False, status=200)
    except:
        Users.objects.create(email=requestData['email'], password=requestData['password'])
        user = Users.objects.values().get(email=requestData['email'])
        payload = GenerateAccessToken(userid=user.get('id'))

        encoded_refresh_Jwt = jwt.encode(payload.get("refreshPayload"), "mrvishope",  algorithm="HS256")
        encoded_access_Jwt = jwt.encode(payload.get("accessPayload"), "mrvishope",  algorithm="HS256")
        response = JsonResponse(payload, safe=False, status=200)
        response.set_cookie('refresh_token', encoded_refresh_Jwt) 
        response.set_cookie('access_token', encoded_access_Jwt)
        print(payload)
        return response
        


def GenerateAccessToken(*args,**kwargs):
    if kwargs.get('userid'):
        userID = kwargs.get('userid')
    if kwargs.get('jti'):
        AccessTokenDB = AccessToken.objects.get(jti=kwargs.get('jti'))
        userID = AccessTokenDB.userid
    access_payload={
        'token_type':'access',
        'jti': math.floor(time.time()  - 100),
        'id':userID,
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
        "accessPayload":access_payload,
        "refreshPayload":refresh_payload
    }
    if  kwargs.get('jti'):        
        AccessTokenDB.jti = kwargs.get('jti')
        AccessTokenDB.userid = access_payload.get('id')
        AccessTokenDB.save()
    else:
        newToken = AccessToken.objects.create(jti=access_payload.get('jti'), userid=access_payload.get('id'))
        newToken.save()
    return payload




def checkToken(token):
    try:
        tk =jwt.decode(token, 'mrvishope', algorithms='HS256')

        return True
    except:
        return False
    
def CheckRefreshAccessToken(refresh_token, access_token):
    check={
        "refreshChecked": True,
        "accessChecked": True

    }
    if refresh_token:
        check['refreshChecked'] = checkToken(refresh_token)
        if check['refreshChecked']:
            if access_token:
                check['accessChecked'] = checkToken(access_token)
            else:
                check['accessChecked'] = False
    else:
        check.refreshChecked = False
    return check


def TokenAuthenticate(func):
    def wrapper(request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")
        access_token = request.COOKIES.get("access_token")
        access = jwt.decode(access_token, 'mrvishope', algorithms='HS256')
        checkToken = CheckRefreshAccessToken(refresh_token, access_token)
        if checkToken.get('refreshChecked'):
            if checkToken.get('accessChecked'):
                    ref = jwt.decode(refresh_token, 'mrvishope', algorithms='HS256')
                    payload = GenerateAccessToken(jti=ref.get('id'))
                    responseData = func(request)
                    # breakpoint()
                    response = {
                            "msg": "Token Authenticated",
                            "status":200,
                            "resData": responseData,
                            "payloadData": payload,

                        }
            else:
                ref = jwt.decode(refresh_token, 'mrvishope', algorithms='HS256')
                payload = GenerateAccessToken()
                access_token = request.COOKIES.get("access_token")
                checkToken = CheckRefreshAccessToken(refresh_token, access_token)
                jwt.decode(access_token, 'mrvishope', algorithms='HS256')
                responseData = func(request)
                response = {
                            "msg": "Token Authenticated",
                            "status": 200,
                            "resData": responseData,
                            "payloadData": payload,
                        }
                
                return response
        else:
            response = {
                            "msg": "Refresh Token Not Authorized",
                            "status": 400,
                            "resData": "asdata",
                            "payloadData": "as",
                        }

        return JsonResponse(response.get('resData'), status=response.get('status'))
    return wrapper



@csrf_exempt
@TokenAuthenticate
def login(request):
    requestData = json.loads(request.body)
    try:
        data =  Users.objects.values().get(email=requestData['email'],is_deleted=False)
        if data['password'] == requestData['password']:
            return data
        else:
            return "Invalid Password"
    except:
        return "Invalid Email"
    
        



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
def getUserData(request, **kwargs):
    userid = kwargs["id"]
    data = Users.objects.values().get(is_deleted=False, id=userid)
    datawithoutPass = {
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
    }
    return JsonResponse(datawithoutPass, safe=False, status=200)




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