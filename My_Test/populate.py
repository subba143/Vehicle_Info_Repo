import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'My_Test.settings')
import django
django.setup()
from Vehicle_App.models import Vehicle
from faker import Faker
from random import *
fake = Faker()
def o_contact():
    d1 = randint(6, 9)
    num = "" + str(d1)
    for i in range(9):
        num = num + str(randint(0, 9))
    return int(num)
def populate(n):
    for i in range(n):
        fvin = fake.vin()
        fmake = fake.random_element(elements=('TATA', 'TOYOTA', 'HONDA ', 'Kia', 'SUN', 'Tesla', 'Mahindra'))
        fmodel = fake.random_element(elements=('TATA_22_Non_AC_White', 'TOYOTA_AC', 'HONDA_Seden ', 'Kia_Cool@143', 'SUN_Hot_24', 'Tesla_7_Sarc', 'MahiRes@123'))
        fyear = fake.random_element(elements=('2022', '2023', '2025 ', '2027', '2028', '2030', '2050'))
        fcolor = fake.color()
        fmileage = fake.random_element(elements=('7000', '10000', '15000 ', '20000', '25000', '27000', '30000'))
        fv_type = fake.random_element(elements=('AC', 'Non_Ac'))
        fseats= fake.random_element(elements=('7', '11', '19 ', '33', '52', '70', '100'))
        fv_seat_type = fake.random_element(elements=('Setting', 'Sleeper', 'Setting & Sleeper'))
        fowner = fake.random_element(elements=('Rattan Tata ', 'Mahindra Varma', 'Subba Reddy', 'Tesla', 'Brothers'))
        fo_contact = o_contact()
        ffeedback = fake.random_element(elements=('GREAT VEHICLE FOR OFFICIAL!', 'EXCELLENT BUT MORE EXPENSIVE', 'GOOD VEHICLE, MORE USEFULLY FOR VACASINAL TRIPS & LESS EXPENSIVE'))

        Vehicles_ADD = Vehicle.objects.get_or_create(
            vin = fvin,
            make = fmake,
            model = fmodel,
            year = fyear,
            color = fcolor,
            mileage = fmileage,
            v_type = fv_type,
            seats = fseats,
            v_seat_type = fv_seat_type,
            owner = fowner,
            o_contact = fo_contact,
            feedback = ffeedback,

            )


n = int(input("Enter number of records:"))
populate(n)
print(f'{n} Records inserted successfully......')

