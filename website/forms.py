from django import forms

class Create_Room_form(forms.Form):
    room_name = forms.CharField(max_length=40,label="Room Name")
    description= forms.CharField(widget=forms.Textarea)
    