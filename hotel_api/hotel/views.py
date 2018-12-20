from .models import Hotel
from django.views import generic
from django.views.generic.edit import CreateView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HotelSerializer

# Create your views here.


class IndexView(generic.ListView) :
    template_name = 'hotel/index.html'
    context_object_name = 'all_hotel'

    def get_queryset (self) :
        return Hotel.objects.all()


class HotelCreate (CreateView) :
    model = Hotel
    fields = ['nama','harga','jumlah_review','lokasi']

class HotelList(APIView) :

    def get (self,request) :
        hotel = Hotel.objects.all()
        serializer = HotelSerializer(hotel, many=True)
        return Response (serializer.data)