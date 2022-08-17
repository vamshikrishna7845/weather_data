from typing_extensions import Required
from urllib import request
from rest_framework import serializers


class WeatherRequest(serializers.Serializer):
    st_date = serializers.IntegerField(required=False)
    end_date = serializers.IntegerField(required=False)
    station_id = serializers.CharField(required=False)