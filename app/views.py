from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from app.services import *
from app.api import *
import base64
from mycolor.models import Image

# Create your views here.

@login_required(login_url="/login")
def getColor(request):
    if request.method == "POST":
        image = request.FILES["image"]
        

      


        season = classify_skin_tone(image)
        Image.objects.create(image=image, user=request.user, season=season)

        # Read the image file and encode it as Base64
        image.seek(0)
        image_data = image.read() #seeking to the beginning of the file before reading:
       
     
        
        encoded_image = base64.b64encode(image_data).decode('utf-8')




        season_name, personal_colors, lipstick_colors = get_season_and_colors(season)
        seasonInfo = SeasonInfo.objects.get(season__name=season_name)
    

      

        return render(request, 'app/colorResult.html',{
            'encoded_image': encoded_image,

            'seasonInfo': seasonInfo,

            "season_name": season_name,
            "personal_colors": personal_colors,
            "lipstick_colors": lipstick_colors
        })
        
    return render(request, 'app/getColor.html')

# def myColor(request):
#     return render(request, 'app/colorResult.html')

@login_required(login_url="/login")
def viewHistory(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'app/history.html', {
        "images": images
    })

@login_required(login_url="/login")
def viewStyle(request):
    return render(request, 'app/getStyle.html')

@login_required(login_url="/login")
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




@login_required(login_url="/login")
def viewColorPalette(request):
    return render(request, 'app/colorPalette.html')