from django.shortcuts import render
import pandas as pd
import json
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px
# from django.http import JsonResponse
from .models import GrossSales

def index(request):
    grosssales = GrossSales.objects.all()
    return render(request, 'fitzforecast/index.html', {'grosssales': grosssales})