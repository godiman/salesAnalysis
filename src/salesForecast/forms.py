from django import forms

from salesForecast.models import (Forcast, Sales)

class ForcastForm(forms.ModelForm):
    
    class Meta:
        model = Forcast 
        
        fields = ('start', 'end')


class SalesForm(forms.ModelForm):
    
    class Meta:
        model = Sales 
        
        fields = ('product', 'amount') 