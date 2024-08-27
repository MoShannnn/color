from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mycolor.models import Image

# Create your views here.

@login_required(login_url="/login")
def getColor(request):
    if request.method == "POST":
        image = request.FILES["image"]
        Image.objects.create(image=image, user=request.user)
        
    return render(request, 'app/getColor.html')

def myColor(request):
    return render(request, 'app/colorResult.html')

def viewHistory(request):
    return render(request, 'app/history.html')

def viewSetting(request):
    return render(request, 'app/setting.html')

def viewColorPalette(request):
    return render(request, 'app/colorPalette.html')