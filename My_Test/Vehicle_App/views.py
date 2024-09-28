from Vehicle_App.models import Vehicle
from django.shortcuts import render, redirect, get_object_or_404
from . forms import VehicleForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def homepage_view(request):
    return render(request, 'Vehicle_Data/index.html')

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'Vehicle_Data/vehicle_list.html', {'vehicles': vehicles})

def vehicle_details(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'Vehicle_Data/vehicle_details.html', {'vehicle': vehicle})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vin = form.cleaned_data['vin']
            make = form.cleaned_data['make']
            model = form.cleaned_data['model']
            year = form.cleaned_data['year']
            color = form.cleaned_data['color']
            mileage = form.cleaned_data['mileage']
            v_type = form.cleaned_data['v_type']
            seats = form.cleaned_data['seats']
            v_seat_type = form.cleaned_data['v_seat_type']
            owner = form.cleaned_data['owner']
            o_contact = form.cleaned_data['o_contact']
            feedback = form.cleaned_data['feedback']
            vehicle = Vehicle.objects.create(vin=vin, make=make, model=model, year=year, color=color, mileage=mileage,
                                             v_type= v_type, seats=seats, v_seat_type=v_seat_type, owner=owner,
                                             o_contact=o_contact, feedback=feedback, )
            return HttpResponseRedirect('/vehicle/{}'.format(vehicle.id))
    else:
        form = VehicleForm()
    return render(request, 'Vehicle_Data/vehicle_add.html', {'form': form})

def vehicle_update(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'Vehicle_Data/vehicle_update.html', {'form': form, 'vehicle': vehicle})

def vehicle_delete(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'Vehicle_Data/vehicle_delete.html', {'vehicle': vehicle})
