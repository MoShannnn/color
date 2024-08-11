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


def view_history(request):
    return render(request, 'app/history.html')