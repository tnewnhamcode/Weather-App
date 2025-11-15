from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status  #is this the issue?
from rest_framework import viewsets
from django.conf import settings
import requests
import os
import json
from django.shortcuts import render
from .models import Weather
from .serializer_models import WeatherSerializer 
import pprint




# Create your views here.

api_key =settings.WEATHER_API_KEY
api_url =settings.WEATHER_API_URL
api_url1=settings.MOROCCO_API_URL
api_url2=settings.NEW_DELHI_API_URL   
api_url3=settings.ISTANBUL_API_URL 
api_url4=settings.BANGKOK_API_URL
api_url5=settings.LISBON_API_URL  
      #it has to be all caps for some reason.. everytihng in settings does

response=requests.get(os.environ['MyVariable1'])

def get_data ():  #used for getting the data- using the key the request the data. (data has now been gotten)
        headers={
            'Authorization':f'Bearer {api_key}',
        }
        response=requests.get(api_url,headers=headers)#you are setting headers which is prusumibly a named argument or whatever you call them (keyword argument la), to the headers dictionary or whatever defined above. its expecting a headers dictionary la
        if response.status_code==200:
            return response.json() #i guess this deserilliazers it. yes it does la. 
            print(f"Error:{response.status_code}")
            return None

def get_data1 ():  #used for getting the data- using the key the request the data. (data has now been gotten)
        headers={
            'Authorization':f'Bearer {api_key}',
        }
        response=requests.get(api_url1,headers=headers)#you are setting headers which is prusumibly a named argument or whatever you call them (keyword argument la), to the headers dictionary or whatever defined above. its expecting a headers dictionary la
        if response.status_code==200:
            return response.json() #i guess this deserilliazers it. yes it does
        else:
            print(f"Error:{response.status_code}")
            return None


def get_data2 ():  #used for getting the data- using the key the request the data. (data has now been gotten)
        headers={
            'Authorization':f'Bearer {api_key}',
        }
        response=requests.get(api_url2,headers=headers)#you are setting headers which is prusumibly a named argument or whatever you call them (keyword argument la), to the headers dictionary or whatever defined above. its expecting a headers dictionary la
        if response.status_code==200:
            return response.json() #i guess this deserilliazers it. 
        else:
            print(f"Error:{response.status_code}")
            return None

def get_data3 ():  #used for getting the data- using the key the request the data. (data has now been gotten)
        headers={
            'Authorization':f'Bearer {api_key}',
        }
        response=requests.get(api_url3,headers=headers)#you are setting headers which is prusumibly a named argument or whatever you call them (keyword argument la), to the headers dictionary or whatever defined above. its expecting a headers dictionary la
        if response.status_code==200:
            return response.json() #i guess this deserilliazers it. yes it does la. . 
        else:
            print(f"Error:{response.status_code}")
            return None


def get_data4 ():  #used for getting the data- using the key the request the data. (data has now been gotten)
        headers={
            'Authorization':f'Bearer {api_key}',
        }
        response=requests.get(api_url4,headers=headers)#you are setting headers which is prusumibly a named argument or whatever you call them (keyword argument la), to the headers dictionary or whatever defined above. its expecting a headers dictionary la
        if response.status_code==200:
            return response.json() #i guess this deserilliazers it. yes it does la.
            print(f"Error:{response.status_code}")
            return None


def get_data5 ():  #used for getting the data- using the key the request the data. (data has now been gotten)
        headers={
            'Authorization':f'Bearer {api_key}',
        }
        response=requests.get(api_url5,headers=headers)#you are setting headers which is prusumibly a named argument or whatever you call them (keyword argument la), to the headers dictionary or whatever defined above. its expecting a headers dictionary la
        if response.status_code==200:
            return response.json() #i guess this deserilliazers it. yes it does la. 
            print(f"Error:{response.status_code}")
            return None
        
class MyModelView(APIView):
    def get(self, request):
        items = Weather.objects.all()  # Fetch all items from the model
        serializer = WeatherSerializer(items, many=True) 
        if serializer.is_valid():#checks if it follows the serializer rules la (they come with them, if it does then it updates the items)
            serializer.save() 
        return Response(serializer.data) #.data` is an attribute of the serializer instance 
                                       #that contains the serialized data. Response is a class that shoots 
                         #a response back to the client who made a request la (its sending the serialized data
                         # this  dont really matter- get that method which you need for weather, i cant remember its name (two of them)
  

    def patch (self, request, pk):    #patch is a class method apparantly. you are defining it within a class here if you look la. 
                                #self is passed so that, if something like 'instance.patch()' is written, then
                                #Python automatically passes the instance as the first argument (which is "self") and thus the stuff is done on the instance
        try:
            item= Weather.objects.get(pk=pk)   #Items usually refers to stuff from your model. the pk for the data your talking about is in the url (what the user searched), so your getting the specific model item based on what the user put in the search bar. (item is like a row or instance, or specific record)
        except Weather.DoesNotExist:       #try is like saying im gonna try this unless a except if a certain error occurs (in this case your model doesnt exist, in whic case do this. i dont get why it aint indented inside try but it aint. theyre sibling blocks la)
            return Response({'detail': 'Weather item not found.'}, status=status.HTTP_404_NOT_FOUND)  
                    
        serializer=WeatherSerializer(item) #specifc record
        data=request.data,#this is what they are sending you. json parsing is handles for you la
        partial=True #means it is just a partial change, not the whole table, just a patch. single row or instance. like all the 'humidity data' for example.)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeatherViewSet(viewsets.ModelViewSet):    #the viewpoint in DRF defines the endpoint.
    queryset=Weather.objects.all()
    serializer_class=WeatherSerializer

    

    def weatherView(self, request):
    # Get the weather data
        weather_data = get_data()
        pprint.pprint(weather_data)  # This line prints to the console
        return render(request, 'London.html', {"weather": weather_data})

    def weatherView1(self, request):
    # Get the weather data
        weather_data = get_data1()
        pprint.pprint(weather_data)  # This line prints to the console
        return render(request, 'MOROCCO.html', {"weather1": weather_data}) 
    
    
    def weatherView2(self, request):
    # Get the weather data
        weather_data = get_data2()
        pprint.pprint(weather_data)  # This line prints to the console
        return render(request, 'New_delhi.html', {"weather2": weather_data}) 
    
    def weatherView3(self, request):
    # Get the weather data
        weather_data = get_data3()
        pprint.pprint(weather_data)  # This line prints to the console
        return render(request, 'Istanbul.html', {"weather3": weather_data}) 
    
    
    def weatherView4(self, request):
    # Get the weather data
        weather_data = get_data4()
        pprint.pprint(weather_data)  # This line prints to the console
        return render(request, 'Bangkok.html', {"weather4": weather_data}) 
    
    def weatherView5(self, request):
    # Get the weather data
        weather_data = get_data5()
        pprint.pprint(weather_data)  # This line prints to the console
        return render(request, 'Lisbon.html', {"weather5": weather_data}) 
    
    








