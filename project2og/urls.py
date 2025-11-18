"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.urls import include
from weather.views import MyModelView
from rest_framework import routers
import weather
from . import settings


router = routers.DefaultRouter()    #Creates a router instance. The `DefaultRouter`
#automatically creates API endpoints for standard set operations (create, read, update, delete).
router.register(r'weather', weather.views.WeatherViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus/', TemplateView.as_view(template_name='aboutus.html')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('weather/', weather.views.MyModelView.as_view(), name='weather-items'),  # URL for MyModelView
    path('weather/', include(router.urls)),  #in this context routers automate the process of giving a url to a viewset (view with method for deleting, editing, creating data from an api all in one) 
    
    path('weather1/', weather.views.WeatherViewSet.as_view({'get': 'weatherView'}), name='London_weather'),
    path('weather2/', weather.views.WeatherViewSet.as_view({'get': 'weatherView1'}), name='Morocco_weather'),
    path('weather3/', weather.views.WeatherViewSet.as_view({'get': 'weatherView2'}), name='NewDehli_weather'),
    path('weather4/', weather.views.WeatherViewSet.as_view({'get': 'weatherView4'}), name='Bangkok_weather'),
    path('weather5/', weather.views.WeatherViewSet.as_view({'get': 'weatherView3'}), name='Istanbul_weather'),
    path('weather6/', weather.views.WeatherViewSet.as_view({'get': 'weatherView5'}), name='Lisbon_weather'),
    #you gotta say as_view() at the end of calling classed based views la (it instatiates it la and the class has got to be given an instance la) 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



