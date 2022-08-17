from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from crop_predictor.models import YieldData


class YieldView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        try:
            queryset = YieldData.objects.all().values('year', 'qty_harvested')
            response_data = dict(status='true', code='200', data=queryset)
            return Response(response_data)
        except Exception as e:
            data = {}
            response_data = dict(status='false', msg=str(e), code='409', data=data)
            return Response(response_data)
