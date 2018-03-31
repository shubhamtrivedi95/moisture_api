from rest_framework import serializers
from . models import Machines
class sensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Machines
        fields=(
            'TokenNo',
            'StackNo',
            'Enable',
            'GrainMoisture',
            'ValueCut',
        )
