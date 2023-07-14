from django import forms
from myapp.models import Zone, Division, SubDivision , Consumer

class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = "__all__"