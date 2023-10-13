from django import forms
from hws.models import Product

class ChoiseForm(forms.Form):
    name = forms.ChoiceField(choices=((1, 'dice'), (2, 'coin'), (3, 'digits')))
    count = forms.IntegerField(min_value=1, max_value=64)
    
class ImageForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    img = forms.ImageField()
    
    