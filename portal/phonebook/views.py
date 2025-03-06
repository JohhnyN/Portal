from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils import timezone
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.http import Http404
from .models import Department, Employee
from .forms import DepartmentForm, EmployeeForm


class DepartmentListView(ListView):
    model = Department
    template_name = "phonebook/department_list.html"
    context_object_name = "departments"

    def get_queryset(self):
        return Department.objects.filter(is_deleted=False)


class DepartmentDetailView(DetailView):
    model = Department
    template_name = "phonebook/department_detail.html"
    context_object_name = "department"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.is_deleted:
            raise Http404("Department does not exist")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employees_count"] = self.get_total_employees_count(self.object)
        return context

    def get_total_employees_count(self, department):
        total_count = department.employees.filter(is_deleted=False).count()
        for child in department.get_children():
            total_count += self.get_total_employees_count(child)
        return total_count


class DepartmentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "phonebook/department_form.html"
    success_url = reverse_lazy("department_list")
    permission_required = "phonebook.add_department"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class DepartmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = "phonebook/department_form.html"
    success_url = reverse_lazy("department_list")
    permission_required = "phonebook.change_department"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.is_deleted:
            raise Http404("Department does not exist")
        return obj

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class DepartmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Department
    template_name = "phonebook/department_confirm_delete.html"
    success_url = reverse_lazy("department_list")
    permission_required = "phonebook.delete_department"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.is_deleted:
            raise Http404("Department does not exist")
        return obj

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.deleted_by = request.user
        self.object.deleted_at = timezone.now()
        self.object.save()
        return redirect(self.success_url)


class EmployeeListView(ListView):
    model = Employee
    template_name = "phonebook/employee_list.html"
    context_object_name = "employees"

    def get_queryset(self):
        return Employee.objects.filter(is_deleted=False)


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "phonebook/employee_detail.html"
    context_object_name = "employee"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.is_deleted:
            raise Http404("Employee does not exist")
        return obj


class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "phonebook/employee_form.html"
    success_url = reverse_lazy("phonebook")
    permission_required = "phonebook.add_employee"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "phonebook/employee_form.html"
    success_url = reverse_lazy("phonebook")
    permission_required = "phonebook.change_employee"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.is_deleted:
            raise Http404("Employee does not exist")
        return obj

    def form_valid(self, form):
        if self.request.POST.get("delete_photo_flag") == "1":
            form.instance.photo.delete()
            form.instance.photo = None
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Employee
    template_name = "phonebook/employee_confirm_delete.html"
    success_url = reverse_lazy("phonebook")
    permission_required = "phonebook.delete_employee"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.is_deleted:
            raise Http404("Employee does not exist")
        return obj

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.deleted_by = request.user
        self.object.deleted_at = timezone.now()
        self.object.save()
        return redirect(self.success_url)
