from django import forms

class PictureForm(forms.Form):
    picfile = forms.FileField(
        label='Select a picture'
    )