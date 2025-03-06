from django import forms
from .models import Department, Employee


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            "department_ru",
            "department_kk",
            "parent",
        ]


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "name_ru",
            "name_kk",
            "position_ru",
            "position_kk",
            "department",
            "email",
            "city_phone_number",
            "mobile_number",
            "order",
            "photo",
        ]
