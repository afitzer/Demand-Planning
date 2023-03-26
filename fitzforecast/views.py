from django.http import JsonResponse
from .models import GrossSales, Product
from .forms import PlanningForm
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.db.models import Q
from datetime import datetime
from django.shortcuts import render
from plotly.offline import plot
from django.core.serializers import serialize
import json
import plotly.express as px
import plotly.graph_objs as go
import plotly
from django.http import HttpResponse


current_year = datetime.now().year

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
        form = PlanningForm()
        data = GrossSales.objects.all()
        product_sales = Product.objects.annotate(
            total_sales=Sum('grosssales__gross_sales'),
            jan_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=1)),
            feb_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=2)),
            mar_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=3)),
            apr_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=4)),
            may_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=5)),
            jun_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=6)),
            jul_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=7)),
            aug_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=8)),
            sep_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=9)),
            oct_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=10)),
            nov_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=11)),
            dec_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=12)),
            ).values('description', 'total_sales', 'grosssales__customer__name', 'jan_sales', 'feb_sales', 'mar_sales', 'apr_sales', 'may_sales', 'jun_sales', 'jul_sales', 'aug_sales', 'sep_sales', 'oct_sales', 'nov_sales', 'dec_sales')
        return render(request, 'fitzforecast/planning.html', {'form': form, 'data': data, 'product_sales': product_sales})
    else:
        form = PlanningForm()
        data = GrossSales.objects.all()
        product_sales = Product.objects.annotate(
            total_sales=Sum('grosssales__gross_sales'),
            jan_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=1)),
            feb_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=2)),
            mar_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=3)),
            apr_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=4)),
            may_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=5)),
            jun_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=6)),
            jul_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=7)),
            aug_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=8)),
            sep_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=9)),
            oct_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=10)),
            nov_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=11)),
            dec_sales=Sum('grosssales__gross_sales', filter=Q(grosssales__date__year=current_year, grosssales__date__month=12)),
            ).values('description', 'total_sales', 'grosssales__customer__name', 'jan_sales', 'feb_sales', 'mar_sales', 'apr_sales', 'may_sales', 'jun_sales', 'jul_sales', 'aug_sales', 'sep_sales', 'oct_sales', 'nov_sales', 'dec_sales')
        return render(request, 'fitzforecast/planning.html', {'form': form, 'data': data, 'product_sales': product_sales})
    
def reports(request):
    product_sales = Product.objects.annotate(
        total_sales=Sum('grosssales__gross_sales')
    ).values('description', 'total_sales')

    x_values = []
    y_values = []
    for sale in product_sales:
        x_values.append(sale['description'])
        y_values.append(sale['total_sales'])

    chart_data = {
        'data': [{
            'x': x_values,
            'y': y_values,
            'type': 'bar'
        }],
        'layout': {
            'xaxis': {'title': 'description'},
            'yaxis': {'title': 'total_sales'},
            'title': 'Sales by Product'
        }
    }

    return HttpResponse(json.dumps(chart_data), content_type='application/json')
