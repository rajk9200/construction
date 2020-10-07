from .models import Payment_Employee
from django import forms
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment_Employee
        fields = '__all__'

