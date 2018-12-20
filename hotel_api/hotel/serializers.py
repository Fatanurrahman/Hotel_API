from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Hotel
        fields = ('nama','harga', 'jumlah_review','lokasi')