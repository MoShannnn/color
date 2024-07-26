from django.shortcuts import render

# Create your views here.
def getColor(request):
    return render(request, 'app/getColor.html')
