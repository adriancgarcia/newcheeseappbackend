from .models import Cheese
from rest_framework import serializers

class CheeseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cheese
        fields = ('id', 'typeofcheese', 'countryoforigin', 'color')

