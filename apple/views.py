from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from apple.models import Apple
from apple.serializers import AppleSerializer

import datetime
import time
import urllib.request
import csv

# Create your views here.
def automatedata():
    date_obj = datetime.datetime.now()
    year=date_obj.year
    month=date_obj.month
    day=date_obj.day
    last_year=int(datetime.datetime(year-1,month,day,0,0,0).timestamp())
    curr_year=int(time.time())
    data_url=f"https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1={last_year}&period2={curr_year}&interval=1d&events=history&includeAdjustedClose=true"
    urllib.request.urlretrieve(data_url,"AAPL.csv")
    Apple.objects.all().delete()
    with open("AAPL.csv","r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            data=Apple(date=row['Date'],open=row['Open'],high=row['High'],low=row['Low'],close=row['Close'],adjclose=row['Adj Close'],volume=row['Volume'])
            data.save()

@api_view(['GET'])
def appleOverview(request):
    apple_urls={
        'List':'/get-data/<string:date>',
    }
    return Response(apple_urls)

@csrf_exempt
def appleApi(request,date="31-12-2021"):
    if request.method=='GET':
        automatedata()
        apples = Apple.objects.filter(date=date)
        apples_serializers=AppleSerializer(apples,many=True)
        return JsonResponse(apples_serializers.data,safe=False)

def getAll(request):
    if request.method=='GET':
        automatedata()
        apples = Apple.objects.all()
        apples_serializers=AppleSerializer(apples,many=True)
        return JsonResponse(apples_serializers.data,safe=False)
