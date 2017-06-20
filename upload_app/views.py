from django.http import JsonResponse
from django.shortcuts import render

from .models import *


def get_password(request):
    try:
        password = request.POST.get('password')

        folder = Folder.objects.get(password=password)

        return JsonResponse(dict(result=str(folder.id)))

    except:
        return "Something went wrong"