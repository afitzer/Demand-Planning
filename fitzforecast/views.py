# import pandas as pd
import json
# from plotly.utils import PlotlyJSONEncoder
# import plotly.express as px
# from django.http import JsonResponse
from plotly.offline import plot
import plotly.graph_objs as go
from django.shortcuts import render
from .models import GrossSales, Product
from .forms import PlanningForm
from django.db.models import Sum

def index(request):
    grosssales = GrossSales.objects.all()
    return render(request, 'fitzforecast/index.html', {'grosssales': grosssales})

def planning(request):
    if request.method == 'POST':
        form = PlanningForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            customer = form.cleaned_data['customer']
            date = form.cleaned_data['date']
            gross_sales = form.cleaned_data['gross_sales']

            GrossSales.objects.create(product=product, customer=customer, date=date, gross_sales=gross_sales)
        else:
            print(form.errors)
        data = GrossSales.objects.all()
        return render(request, 'fitzforecast/planning.html', {'form': form, 'data': data})
    else:
        form = PlanningForm()
        data = GrossSales.objects.all()
        product_sales = Product.objects.annotate(total_sales=Sum('grosssales__gross_sales')).values('description', 'total_sales')
        return render(request, 'fitzforecast/planning.html', {'form': form, 'data': data, 'product_sales': product_sales})
    
def reports(request):
    product_sales = Product.objects.annotate(total_sales=Sum('grosssales__gross_sales')).values('description', 'total_sales')

    data = [
        go.Bar(
            x=[item['description'] for item in product_sales],
            y=[item['total_sales'] for item in product_sales]
        )
    ]
    graphJSON = plot(data, output_type='json', auto_open=False)

    context = {
        'graphJSON': graphJSON
    }
    return render(request, 'fitzforecast/reports.html', context)
