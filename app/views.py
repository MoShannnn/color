from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mycolor.models import Image
from django.http import HttpResponseRedirect
from app.services import *
from app.api import *
import base64
# Create your views here.

@login_required(login_url="/login")
def getColor(request):
    if request.method == "POST":
        image = request.FILES["image"]
      


        season = classify_skin_tone(image)


        season_name, personal_colors, lipstick_colors = get_season_and_colors(season)
        # Read the image file and encode it as Base64
        image.seek(0)
        image_data = image.read() #seeking to the beginning of the file before reading:
       
     
        
        encoded_image = base64.b64encode(image_data).decode('utf-8')


        return render(request, 'app/colorResult.html',{
            'encoded_image': encoded_image,
            "season_name": season_name,
            "personal_colors": personal_colors,
            "lipstick_colors": lipstick_colors
        })
        
    return render(request, 'app/getColor.html')

# def myColor(request):
#     return render(request, 'app/colorResult.html')

def viewHistory(request):
    return render(request, 'app/history.html')

def viewStyle(request):
    return render(request, 'app/getStyle.html')

def viewSetting(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST["username"]
        user.email = request.POST["email"]
        user.save()

# def viewResult(request, image, season_name, personal_colors, lipstick_colors):


#     return render(request, 'app/colorResult.html',{
#             'image': image,
#             "season_name": season_name,
#             "personal_colors": personal_colors,
#             "lipstick_colors": lipstick_colors
#         })
        


    username = request.user.username
    email = request.user.email
    
    return render(request, 'app/setting.html',{
            "username": username,
            "email": email

        })





def viewColorPalette(request):
    return render(request, 'app/colorPalette.html')