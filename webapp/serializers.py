from rest_framework import serializers
from . models import sensors
class sensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=sensors
        fields=(
            'roomNo',
            'sensorId',
            'sensorValue',
        )
