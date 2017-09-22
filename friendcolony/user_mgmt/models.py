from django.contrib.auth.models import User
from django.db import models	
import datetime
class User_Profile(models.Model):
    user = models.OneToOneField(User)
    #name = models.TextField(max_length=100)
    #email = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    contact_no  = models.CharField(max_length=20)
    website = models.CharField(max_length=20 ,blank=True)
    #PlaceId = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True)


class HangOutPlaces(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null=True, blank=True)
    Area = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    ContactNo = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Website = models.CharField(max_length=50, null=True, blank=True)
    PlaceId = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True)

class CricketHangOutPlace(models.Model):
    hangoutplaces = models.ForeignKey(HangOutPlaces, on_delete=models.CASCADE)
    GroundName = models.CharField(max_length=50, null=True, blank=True)
    AboutGround = models.CharField(max_length=300, null=True, blank=True)
    Width = models.CharField(max_length=50, null=True, blank=True)
    Length = models.CharField(max_length=50, null=True, blank=True)
    TotalArea = models.CharField(max_length=50, null=True, blank=True)
    PitchSize = models.CharField(max_length=50, null=True, blank=True)
    NumberOfPitch = models.IntegerField(null=True, blank=True)
    BallingMachin = models.BooleanField(default=False)
    NetPractiseArea = models.CharField(max_length=50, null=True, blank=True)
    Capacity = models.IntegerField(null=True, blank=True)
    AnyOtherInfo = models.CharField(max_length=200,null=True, blank=True)
    SubsAndPacks = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True)



