# from django import forms
# from .models import Vehicle
#
# class VehicleForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(VehicleForm, self).__init__(*args, **kwargs)
#         self.fields['vin'].required = True
#         self.fields['make'].required = True
#         self.fields['model'].required = True
#         self.fields['owner'].required = True
#         self.fields['o_contact'].required = True
#
#     class Meta:
#         model = Vehicle
#         fields = '__all__'



from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.fields['vin'].required = True
        self.fields['make'].required = True
        self.fields['model'].required = True
        self.fields['owner'].required = True
        self.fields['o_contact'].required = True

    class Meta:
        model = Vehicle
        fields = ['vin', 'make', 'model', 'owner', 'o_contact']  # Specify only required fields
