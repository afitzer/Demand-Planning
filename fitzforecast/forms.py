from django import forms
from .models import Product, Customer

class PlanningForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Year", "Month", "Day")), initial="YYYY-MM-01")
    gross_sales = forms.IntegerField(required=True, help_text='This is monthly gross sales planning. Put the 1st day of the planning month.')