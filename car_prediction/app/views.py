from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car, Route, uploaded
import folium
import pandas as pd
from .forms import CSVUploadForm


# Create your views here.

def index(request):
    return HttpResponse("Server is up and running")


def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = uploaded(file=request.FILES['csv_file'])
            uploaded_file.save()
            print("File uploaded successfully")
            return redirect('dashboard')
    else:
        form = CSVUploadForm()
    return render(request, 'dashboard/upload.html', {'form': form})


def dashboard(request):
    car = Car.objects.first()
    route = Route.objects.filter(car=car).first()

    # Map using foliujm
    m = folium.Map(location=[43.7, -79.4], zoom_start=12)

    if route:
        folium.PolyLine(route.coordinates).add_to(m)

    m = m._repr_html_()
    context = {
        'car': car,
        'map': m
    }

    return render(request, 'dashboard/car_dashboard.html', context)
