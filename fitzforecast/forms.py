from django import forms
from .models import Product, Customer, GrossSales

class PlanningForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    date = forms.DateField()
    gross_sales = forms.IntegerField()