from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mycolor.models import Image
from django.http import HttpResponseRedirect
from app.services import *
# Create your views here.

@login_required(login_url="/login")
def getColor(request):
    if request.method == "POST":
        image = request.FILES["image"]
        season = "True Spring"
        Image.objects.create(image=image, user=request.user, season=season)
        season_name, personal_colors, lipstick_colors = get_season_and_colors(season)


        return render(request, 'app/colorResult.html',{
            "season_name": season_name,
            "personal_colors": personal_colors,
            "lipstick_colors": lipstick_colors
        })
        
    return render(request, 'app/getColor.html')

def myColor(request):
    return render(request, 'app/colorResult.html')

def viewHistory(request):
    return render(request, 'app/history.html')

def viewSetting(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST["username"]
        user.email = request.POST["email"]
        user.save()
    

    username = request.user.username
    email = request.user.email
    
    return render(request, 'app/setting.html',{
            "username": username,
            "email": email

        })





def viewColorPalette(request):
    return render(request, 'app/colorPalette.html')