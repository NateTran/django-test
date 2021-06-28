from django import forms

from .models import testapp 

class testappForm(forms.ModelForm):
    class Meta:
        model = testapp
        fields = [
                'title',
                'description',
                'price'
        ]

class RawForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()

