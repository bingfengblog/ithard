from django import forms
from hardware.models import City,User,Item,Depart

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('cityname',)
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'