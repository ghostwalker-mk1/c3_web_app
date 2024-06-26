from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import Inventory, Warranty, Sale, SaleItem, Claim, Inspection, UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'name', 'address', 'city', 'province', 'postal_code']

    class ChangePasswordForm(PasswordChangeForm):
        pass

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product_id', 'name', 'quantity', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer_name', 'customer_contact', 'dealership_details', 'sales_rep_name', 'sales_rep_contact', 'sales_region']

class SaleItemForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Inventory.objects.all())

    class Meta:
        model = SaleItem
        fields = ['product', 'quantity']

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['claim_type', 'status', 'customer_name', 'dealership_details']

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['location', 'inspection_type', 'make', 'model', 'year', 'vin', 'comments']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 3}),
        }

class WarrantyForm(forms.ModelForm):
    class Meta:
        model = Warranty
        fields = ['product_name', 'serial_number', 'purchase_date', 'expiration_date', 'comments']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 3}),
        }