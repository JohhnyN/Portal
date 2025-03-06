from django.urls import include, path
from .views import (
    DepartmentListView,
    DepartmentDetailView,
    EmployeeDetailView,
    DepartmentCreateView,
    DepartmentUpdateView,
    DepartmentDeleteView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    EmployeeListView,
)

urlpatterns = [
    path("phonebook/", EmployeeListView.as_view(), name="phonebook"),
    path("departments/", DepartmentListView.as_view(), name="department_list"),
    path(
        "departments/<int:pk>/",
        DepartmentDetailView.as_view(),
        name="department_detail",
    ),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee_detail"),
    path("departments/add/", DepartmentCreateView.as_view(), name="department_add"),
    path(
        "departments/update/<int:pk>/",
        DepartmentUpdateView.as_view(),
        name="department_update",
    ),
    path(
        "departments/delete/<int:pk>/",
        DepartmentDeleteView.as_view(),
        name="department_delete",
    ),
    path("employees/add/", EmployeeCreateView.as_view(), name="employee_add"),
    path(
        "employees/update/<int:pk>/",
        EmployeeUpdateView.as_view(),
        name="employee_update",
    ),
    path(
        "employees/delete/<int:pk>/",
        EmployeeDeleteView.as_view(),
        name="employee_delete",
    ),
]
