from rest_framework import serializers
from .models import cars

class Serializer_Cars(serializers.ModelSerializer):

    class Meta:
        model = cars
        fields = ('name','band','color','price',)