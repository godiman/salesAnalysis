import csv
from django.shortcuts import render, redirect
from salesForecast.forms import (ForcastForm, SalesForm)
from salesForecast.forecast import forecastSales
from salesForecast.models import Sales
from account.models import Account
import datetime
import os
from csv import writer


# Create your views here.

def home_view(request):
     
    context = {}
    # Checks if the user is login
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.POST:
        # Instantiate the form
        form = ForcastForm(request.POST)
        
        # checks if the form imput is valid
        if form.is_valid(): 
            print(form.cleaned_data)
            
            # Gets the form values
            start_date = form.cleaned_data['start']
            end_date = form.cleaned_data['end']
            # print(start_date, end_date) 
            forecast = forecastSales(start_date, end_date)
            context['forecast'] = forecast
        else:   
            form = ForcastForm()
            context['form']  = form
            
    return render(request, 'salesForcast/home.html', context)


def sales_view(request):
    context = {}
    # Checks if the user is login
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.POST:
        # Instantiate the form
        form = SalesForm(request.POST)
        
        # checks if the form imput is valid
        if form.is_valid(): 
            # print(form.cleaned_data)
            
            # Get the current date
            month = datetime.date.today()
            p = form.cleaned_data['product']
            m = form.cleaned_data['amount']
            # Create the sales
            user = Account.objects.filter(id=request.user.id).first()
            # print(user)
            s = Sales.objects.create(user=user, product=p, amount=m, month=month)
            
            # Get the absolute data path
            data_path = os.path.abspath('data/forecast.csv') 
            
            # with open(data_path, 'a',newline='') as File:
            #     writer = csv.writer(File)
            #     writer.writerow([month, m])
            #     File.close()
    # Load the dataset
            if s: 
                context['success'] = True
        else:   
            form = SalesForm()
            context['form']  = form
    return render(request, 'salesForcast/sales.html', context)

def all_sales_view(request):
    
    context = {}
    
    # Checks if the user is login
    if not request.user.is_authenticated:
        return redirect('login')
    
    
    sales = Sales.objects.all()
    
    context['all_sales'] = sales
    
    return render(request, 'salesForcast/all_sales.html', context)