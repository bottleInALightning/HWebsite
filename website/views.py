from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Create_Room_form
import string
from random import choice
from .models import *
# Create your views here.

def get_suffix(length):
    room_suffix=""
    char_set=string.ascii_lowercase+"1234567890"
    for i in range(length): #six is the length of characers forming the suffix
        room_suffix+=choice(char_set)
    return room_suffix


def create_room_database_entry(request, room_name, room_description):
    class_room = Class_Room( name=room_name,
                            description=room_description,
                            creator_id=request.user.id)
    class_room.save()
    
    final_suffix=""
    while True:
        temp_suffix=get_suffix(6)
        if Class_Room.objects.filter(link_suffix=temp_suffix) >0:
            continue
        else:
            final_suffix=temp_suffix
            print("Final suffix is:",final_suffix)
            break
    
    class_room.link_suffix=final_suffix
    class_room.save()

    
    print("Room created successfully!")

    
def homepage(request):
    context={}
    return render(request,"website/homepage.html",context)#

def create_room(request):
    if request.method=="POST":
        form = Create_Room_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("Form data:",data)
            create_room_database_entry(request,data.get("room_name"),data.get("description"))


    else:
        name_form=Create_Room_form()
    context={"form":name_form}
    return render(request,"website/create_room.html",context)

def classroom(request):
    return render(request,"website/")