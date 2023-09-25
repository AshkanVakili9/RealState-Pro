from rest_framework import generics
from rest_framework.response import Response

from listings.models import Listings
from .serializers import ListingsSerializer


class ListingList(generics.ListAPIView):
    queryset = Listings.objects.all().order_by('-date_posted')
    serializer_class = ListingsSerializer


class ListingCreate(generics.CreateAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingsSerializer
    
class ListingDetail(generics.RetrieveAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingsSerializer


class ListingDelete(generics.DestroyAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingsSerializer
    
    
class ListingUpdate(generics.UpdateAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingsSerializer
