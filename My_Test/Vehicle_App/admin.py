from django.contrib import admin
from Vehicle_App.models import Vehicle
# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vin', 'make', 'model', 'year', 'color', 'mileage', 'v_type', 'seats', 'v_seat_type', 'owner', 'o_contact', 'feedback']
admin.site.register(Vehicle,VehicleAdmin)
