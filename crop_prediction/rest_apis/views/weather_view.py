from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from crop_prediction.rest_apis.request import WeatherRequest
from crop_predictor.models import WeatherData


class WeatherView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        try:
            request_data = request.GET
            req_data = WeatherRequest(data=request_data)
            if req_data.is_valid():
                req_data = req_data.validated_data
                if req_data.get("station_id") and req_data.get("st_date") and req_data.get("end_date"):
                    queryset = WeatherData.objects.filter(weather_station=req_data['station_id'], date__gte=req_data['st_date'], date__lte=req_data['end_date'])
                elif req_data.get("station_id") and req_data.get("st_date"):
                    queryset = WeatherData.objects.filter(weather_station=req_data['station_id'], date__gte=req_data['st_date'])
                elif req_data.get("station_id") and req_data.get("end_date"):
                    queryset = WeatherData.objects.filter(weather_station=req_data['station_id'],date__lte=req_data['end_date'])
                elif req_data.get("station_id"):
                    queryset = WeatherData.objects.filter(weather_station=req_data['station_id'])
                else:
                    queryset = WeatherData.objects.all()
                queryset = queryset.values("max_temp", "min_temp", "precipitation", "weather_station", "date")
                return Response(queryset)
            else:
                return Response({"status": 409, "msg": req_data.is_valid(raise_exception=True)})
        except Exception as e:
            data = {}
            response_data = dict(status='false', msg=str(e), code='409', data=data)
            return Response(response_data)
