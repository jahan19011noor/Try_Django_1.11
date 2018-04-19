from django import forms
from .models import Restaurant
from .validators import validate_caterogy, validate_email

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
    # email = forms.EmailField()
    # if v validator added to model field itself in models.py then the followin line is not needed
        # category = forms.CharField(required=False, validators=[validate_caterogy])
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

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if ".edu" in email:
    #         raise forms.ValidationError("Invalid Email");
    #     return email

