from django import forms
from forensic.models import *


class bodydetailsForm(forms.ModelForm):
    class Meta:
        model = bodydetails
        fields = [ 'name','bid','age', 'gender', 'weight', 'blood', 'evidence', 'body']
