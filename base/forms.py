from tkinter.tix import Form
from .models import Room
from django.forms import ModelForm

class RoomForm(ModelForm ):
    class Meta:
        model= Room
        fields= '__all__'