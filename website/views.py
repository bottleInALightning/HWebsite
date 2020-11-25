from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test_view(request):
    context={"dummy":2}
    return render(request,"website/homepage.html",context)

def classroom(request):
    return render(request,"website/")