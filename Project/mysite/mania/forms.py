
from django import forms

# creating a form 
class bookingForm(forms.Form):
   
    Court_name = forms.CharField(max_length = 200)
    Court_fee = forms.CharField(max_length = 200)

# import GeeksModel from models.py
from .models import Account, Booking
  
# create a ModelForm
class BookingForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Booking
        fields = ['account','court','booked_from', 'booked_to']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["account"].widget=forms.HiddenInput()
        self.fields["booked_from"].widget=forms.SelectDateWidget()
        self.fields["booked_to"].widget=forms.SelectDateWidget()