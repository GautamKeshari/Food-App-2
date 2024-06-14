from django import forms
# we are creating forms for items 
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['item_name','item_desc','item_price','item_image'] 