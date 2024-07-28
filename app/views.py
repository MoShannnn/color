from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def getColor(request):
    return render(request, 'app/getColor.html')
