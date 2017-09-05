from django.http import JsonResponse
from django.shortcuts import render

from .models import *


def get_password(request):
    try:
        password = request.GET.get('password')
        login = request.GET.get('login')

        folder = Folder.objects.get(password=password, login=login)
        return JsonResponse(dict(result=folder.id))

    except:

        return JsonResponse(dict(result="Something went wrong"))
