import json
from datetime import datetime
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

def api_view(request):
    if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        form.save()
        return JsonResponse({"success":True}, status=200)
    return JsonResponse({"success":False}, status=400)




ERROR = {
            "error": "Division by zero!"
        }


def isNum(answer):
    try:
        int(answer)
        return (True)
    except ValueError:
        return (False)

def add_api(request, *args, **kwargs):
    answer = {
        "A": 1234,
        "B": 4567,
    }

    if isNum(answer['A'])==True and isNum(answer['B'])==True :
        answer = QueryDict.fromkeys(['answer'], value=answer['A']+answer['B'])
    else:
        answer = JsonResponse(ERROR)
        answer.status_code = 403
        return answer
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response


def subtract_api(request, *args, **kwargs):
    answer = {
        "A": 1234,
        "B": 4567,
    }
    if isNum(answer['A'])==True and isNum(answer['B'])==True :
        answer = QueryDict.fromkeys(['answer'], value=answer['A']-answer['B'])
    else:
        answer = JsonResponse(ERROR)
        answer.status_code = 403
        return answer
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response

def multiply_api(request, *args, **kwargs):
    answer = {
        "A": 1234,
        "B": 4567,
    }
    if isNum(answer['A'])==True and isNum(answer['B'])==True :
        answer = QueryDict.fromkeys(['answer'], value=answer['A']*answer['B'])
    else:
        answer = JsonResponse(ERROR)
        answer.status_code = 403
        return answer
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response

def divide_api(request, *args, **kwargs):
    answer = {
        "A": 1234,
        "B": 4567,
    }
    if isNum(answer['A'])==True and isNum(answer['B'])==True :
        answer = QueryDict.fromkeys(['answer'], value=answer['A']/answer['B'])
    else:
        answer = JsonResponse(ERROR)
        answer.status_code = 403
        return answer
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response




