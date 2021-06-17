from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import cars
from .serializers import Serializer_Cars
# Create your views here.

class CarsView(APIView):
    # def get(self,request):
    #     list_cars = cars.objects.all()
    #     datas = Serializer_Cars(list_cars, many=True)
    #     return Response(data=datas.data,status=status.HTTP_200_OK)

    # def post(self,request):
    #     post_data = Serializer_Cars(data=request.data)
    #     if post_data.is_valid():
    #         post_data.save()
    #         return Response(data=datas,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(post_data.errors,status=status.HTTP_400_BAD_REQUEST)

#-------------get_data_from_DB-----------------------#
    def get(self,request):
        list_cars = cars.objects.all()
        car_data = Serializer_Cars(list_cars,many=True)
        return Response(data=car_data.data,status=status.HTTP_200_OK)

#-------------post_data_into_DB-----------------------#
    def post(self,request):
        car_data = Serializer_Cars(data = request.data)
        if car_data.is_valid():
            name = car_data.data['name']
            band = car_data.data['band']
            color = car_data.data['color']
            price = car_data.data['price']
            post_data = cars.objects.create(name=name,band=band,color=color,price=price)
            return Response(data=post_data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=car_data.errors,status=status.HTTP_400_BAD_REQUEST)