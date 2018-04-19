from django import forms
from .models import Restaurant

class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get("name");
        if name=="hellow":
            raise forms.ValidationError("Not a Valid Name")
        return name

class RestaurantCreateModelForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'location',
            'category'
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name");
        if name=="hellow":
            raise forms.ValidationError("Not a Valid Name")
        return name