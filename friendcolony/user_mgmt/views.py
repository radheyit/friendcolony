from django.shortcuts import render
#from user.models import User_Profile
#from user.serializers import User_Profile_Serializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import User_Profile
from .models import HangOutPlaces
from .models import CricketHangOutPlace

def cricket():
    print ("in the function")

def CricketAddHangOUtPlace(request):
    print(request)
    try:
        print("In the function" + request.POST.get('name'))
    except:
        print("Error in the getting ")
    

@api_view(['POST'])
def registration_api(request,pk):
    if request.method=='POST':
        print("IN a Function")
        user = User.objects.get(pk = pk)
        name = request.POST.get('name')
        area = request.POST.get('area')
        address = request.POST.get('address')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        website = request.POST.get('website')
        print("Address:"+ address +"  name:"+ name +"  contact_no:"+ contact_no +"  area:"+ area)
        obj = HangOutPlaces(user=user, Name=name, Area=area, Address=address, ContactNo=contact_no, Email=email, Website=website)
        obj.save()
        if(obj):
            print("YA Fine OBJ FIRST")
        else:
            print("No Wrong OBJ FIRST")
        GroundName = request.POST.get('groundname')
        AboutGround = request.POST.get('aboutground')
        Width = request.POST.get('width')
        Length = request.POST.get('length')
        TotalArea = request.POST.get('totalarea')
        PitchSize = request.POST.get('pitchsize')
        NumberOfPitch = request.POST.get('numberofpitch')
        BallingMachin = request.POST.get('ballingmachin')
        NetPractiseArea = request.POST.get('netpractisearea')
        Capacity = request.POST.get('capacity')
        AnyOtherInfo = request.POST.get('anyotherinfo')
        SubsAndPacks = request.POST.get('subsandpacks')
        obj2 = CricketHangOutPlace(hangoutplaces=obj, GroundName=GroundName, AboutGround=AboutGround, Width=Width, Length=Length, TotalArea=TotalArea, PitchSize=PitchSize, NumberOfPitch=NumberOfPitch, NetPractiseArea=NetPractiseArea, Capacity=Capacity, AnyOtherInfo=AnyOtherInfo)
        obj2.save()
        if(obj2):
            print("OK obj2")
        else:
            print("No Wrong")
@api_view(['GET','POST'])
def login_api(request):
    print("in login")
    print(request.data)
    email = request.POST.get('email')
    passw = request.POST.get('password')
    uname= request.POST.get('uname')
    print(email,passw,uname)
    #user_obj = User(username=uname)
    #user_obj.set_password(passw)
    #user_obj.save()
    user_obj = User.objects.create_user(username=uname,email=email,password=passw)
    user_obj.save()
    print(user_obj.password)
    isuser = User.objects.filter(email = email, password = passw).exists()
    print(isuser)
    return Response(user_obj.password,status=status.HTTP_200_OK)
	
    try:
        if User.objects.get(username=email) and User.objects.get(password = passw):
            return ({"result":True})
    except:
        return ({"result":False})
    return ({"result":False})