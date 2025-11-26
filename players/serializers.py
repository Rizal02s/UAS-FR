from rest_framework import serializers
from .models import Pemain

class PemainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemain
        fields = '__all__'