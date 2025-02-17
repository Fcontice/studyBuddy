from django.forms import ModelForm
from base.models import Room, Topic, Message

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = [ 'host', 'particpants']