"""crop_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from crop_prediction.rest_apis.views import YieldView, StatisticsView, WeatherView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/weather", WeatherView.as_view(), name='weather_data'),
    path("api/yield", YieldView.as_view(), name="yield_data"),
    path("api/weather/stats", StatisticsView.as_view(), name="weather_stats")
]
