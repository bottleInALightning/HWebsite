from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test_view(request):
    context={"dummy":2}
    return render(request,"website/homepage.html",context)#

def create_room(request):
    context={"dummy":2}
    return render(request,"website/create_room.html",context)

def classroom(request):
    return render(request,"website/")