from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from crop_predictor.models import StatisticsData


class StatisticsView(GenericAPIView):

    # pagination_class = pagination.PageNumberPagination

    def get(self, request, *args, **kwargs):
        try:
            queryset = StatisticsData.objects.all().values("max_temp", "min_temp", "precipitation", "weather_station", "year")
            response_data = dict(status='true', code='200', data=queryset)
            return Response(response_data)
        except Exception as e:
            data = {}
            response_data = dict(status='false', msg=str(e), code='409', data=data)
            return Response(response_data)
