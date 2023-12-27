from rest_framework import serializers
from .models import modelo


class serializerModelo (serializers.ModelSerializer):
    class Meta:
        model = modelo
        fields = '__all__'
        read_only_fields = ('fecha',)

        # read_only_fields = ('fecha',)  lleva una coma  para que lo lea como TUPLA de lo contrario lo lee como un String