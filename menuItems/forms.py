from django import forms
from .models import MenuItem
from restaurants.models import Restaurant

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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(MenuItemCreateModelForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = Restaurant.objects.filter(owner=user)#, menuitem__isnull=True)#.exclude(menuitem__isnull=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name == 'No Restaurant':
            raise forms.ValidationError('Not a valid Restaurant Name')

        return name