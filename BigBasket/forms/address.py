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
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter fullname', 'width':'200px'}),
			'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter street'}),
			'landmark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter landmark'}),
			'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter city'}),
			'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter pincode'}),
			'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter state'}),
            'country':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'enter country'  }),
            'mobileno':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter mobile no'}),
            'address_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter address type'}),
        }