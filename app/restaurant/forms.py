from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'desc', 'price')
    
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.label == "Name":
                visible.field.widget.attrs['placeholder'] = "Item Name"
            elif visible.label == "Desc":
                visible.field.widget.attrs['placeholder'] = "Item Description"
            elif visible.label == "Price":
                visible.field.widget.attrs['placeholder'] = "Item Price (USD)"
                