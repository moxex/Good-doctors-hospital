from django.shortcuts import render, redirect
from .models import Department
from users.models import User
from django.views.generic import ListView, DetailView, TemplateView

STATUS = [
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
    ('Human Resource', 'Human Resource'),
]

# Home View
class HomeView(ListView):
    template_name = 'hospital/home.html'
    queryset = Department.objects.all()
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['experts', 'doctors', 'user'] = User.objects.all()
        return context


# Department List Views
class DepartmentListView(ListView):
    queryset = Department.objects.all()
    template_name = "hospital/departments.html"

# Department Detail View
class DepartmentDetailView(DetailView):
    queryset = Department.objects.all()
    template_name = "hospital/department_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['departments'] = Department.objects.all()
        return context
