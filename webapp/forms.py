from django import forms

from . models import Machines
class GetData(forms.ModelForm):
    class Meta:
        model=Machines
        fields=[
            'TokenNo',
            'StackNo',
        ]

class ShowData(forms.ModelForm):
    class Meta:
        model=Machines
        fields=[
            'TokenNo',
            'StackNo',
        ]