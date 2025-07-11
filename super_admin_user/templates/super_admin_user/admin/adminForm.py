from django import forms
from super_admin_user.models import AdminUserList
from django.core.exceptions import ValidationError
import re

def validate_org_id(value):
 
    if not re.fullmatch(r'^[a-z_]+$', value):
        raise ValidationError("Only lowercase letters and underscores are allowed.")

class AdminUserForm(forms.ModelForm):
    org_id = forms.CharField(
        max_length=100,  # Set appropriate max length
        validators=[validate_org_id],  # Attach custom validator
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'pattern': '^[a-z_]+$',  # Front-end validation (optional)
            'title': 'Only lowercase letters and underscores are allowed.'
        })
    )

    class Meta:
        model = AdminUserList
        fields = ['org_id', 'name', 'email', 'password', 'username', 'address', 'mobile', 'superadmin_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'superadmin_id': forms.Select(attrs={'class': 'form-control'}),
        }