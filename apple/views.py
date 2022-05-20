from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from apple.models import Apple
from apple.serializers import AppleSerializer

# Create your views here.
@api_view(['GET'])
def appleOverview(request):
    apple_urls={
        'List':'/get-data/<string:date>',
    }
    return Response(apple_urls)

@csrf_exempt
def appleApi(request,date="31-12-2021"):
    if request.method=='GET':
        apples = Apple.objects.filter(date=date)
        apples_serializers=AppleSerializer(apples,many=True)
        return JsonResponse(apples_serializers.data,safe=False)

def getAll(request):
    if request.method=='GET':
        apples = Apple.objects.all()
        apples_serializers=AppleSerializer(apples,many=True)
        return JsonResponse(apples_serializers.data,safe=False)
