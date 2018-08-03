from BigBasket.models import Address
from django import  forms


class AddressForm(forms.ModelForm):
    mobileno = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mobileno'}),
                                help_text=(
                                    "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")),

    class Meta:
        model = Address
        exclude= ['id','user']

        # fields = ('country', 'fullname', 'pincode','street','mobileno','landmark','city','state','address_type' , )
        widgets={
            'country':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'enter title'  }),
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'mobileno':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'landmark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'address_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
        }