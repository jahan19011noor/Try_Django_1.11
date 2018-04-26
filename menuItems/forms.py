from django import forms
from .models import MenuItem

class MenuItemCreateForm(forms.Form):
    # menuItem fields
    restaurant  = forms.IntegerField(required=True)
    name        = forms.CharField(required=True)
    contents    = forms.CharField()
    excludes    = forms.CharField()
    public      = forms.BooleanField()

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name=='No Restaurant':
            raise forms.ValidationError("Not a valid Restaurant Name")
        return name

class MenuItemCreateModelForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name == 'No Restaurant':
            raise forms.ValidationError('Not a valid Restaurant Name')

        return name