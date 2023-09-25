from rest_framework import serializers
from users.models import Profile
from listings.models import Listings
from listings.api.serializers import ListingsSerializer

class ProfileSerializer(serializers.ModelSerializer):
    seller_listings= serializers.SerializerMethodField()
    
    def get_seller_listings(self, obj):
        listings = Listings.objects.filter(seller=obj.seller)
        listings_serialized = ListingsSerializer(listings, many=True).data
        return listings_serialized
    
    
    class Meta:
        model = Profile
        fields = '__all__'
