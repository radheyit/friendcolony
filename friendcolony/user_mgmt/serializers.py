from rest_framework import serializers
from user.models import User_Profile
from django.contrib.auth.models import User

class User_Serializer(serializers.serializer):
    class Meta:
        models = User
        fields = (first_name,last_name,email,password)

class UserProfileSerializer(serializers.serializer):
    #firstname  = serializer.	
    class Meta:
        models = User_Profile
        fields = (name,area,address,contact_no,email,website)

class HangOutPlacesSerializer(serializers.serializer):
    class Meta:
        models = HangOutPlaces
        fields = (user, Name, Area, Address, ContactNo, Email, Website, PlaceId)
class CricketHangOutPlaceSerializer(serializers.serializer):
    class Meta:
        models = hangOutPlaces
        fields = (hangoutplaces, GroundName, AboutGround, Width, Length, TotalArea, PitchSize, NumberOfPitch, BallingMachin, NetPractiseArea, Capacity, AnyOtherInfo, SubsAndPacks)