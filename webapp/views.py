from django.http import HttpResponse

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . serializers import sensorsSerializer
from . models import sensors
from django.shortcuts import get_object_or_404
class sensorList(generics.ListCreateAPIView):

    queryset = sensors.objects.all()
    serializer_class = sensorsSerializer
    lookup_url_kwarg = "rm_No"


class uniqueSensorList(generics.ListCreateAPIView):

    queryset = sensors.objects.all()
    serializer_class = sensorsSerializer
    lookup_url_kwarg = "rm_No"

    def get_queryset(self):
        rm_No = self.kwargs.get(self.lookup_url_kwarg)
        return self.queryset.filter(roomNo=rm_No)





class MultiOperation(generics.UpdateAPIView):

    queryset = sensors.objects.all()
    serializer_class = sensorsSerializer
    lookup_url_kwarg = "rm_No"
    def get_queryset(self):
        rm_No = self.kwargs.get(self.lookup_url_kwarg)
        return self.queryset.filter(roomNo=rm_No)

    def perform_update(self, serializer):
        sensor=get_object_or_404(
            sensors,roomNo=self.kwargs.get(self.lookup_url_kwarg)
        )
        serializer.save(sensor=sensor)

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            roomNo=self.kwargs.get(self.lookup_url_kwarg)
        )
    #
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

# from rest_framework.decorators import APIView,api_view
# from rest_framework.response import Response
# from rest_framework import status
# from . serializers import sensorsSerializer
# from . models import sensors
# @lookup_url_kwarg = "rm_No"
# def get(request,format=None):
#     sensor=sensors.objects.all()
#     serializer=sensorsSerializer(sensor,many=True)
#     return Response(serializer.data)
#
# def post(request,format=None):
#     serializer = sensorsSerializer(data=request.data, many=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data,status=status.HTTP_201_CREATED)
#
#
# def user_update(request, ):
#
#     user = sensors.objects.get(roomNo=rm_No)
#     if request.method == "PUT":
#         serializer = sensorsSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response({"error": serializer.errors, "error": True})
#     serializer = sensorsSerializer(user)
#     return Response(serializer.data)


def welcome(request):
    return HttpResponse("<h2> Moisture Meter API.<h2>")