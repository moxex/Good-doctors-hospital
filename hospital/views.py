from multiprocessing import context
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Department
from users.models import User
from django.views.generic import ListView, DetailView, TemplateView
from users.models import DoctorProfile
from blog.models import Post

STATUS = [
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
    ('Human Resource', 'Human Resource'),
]


def home(request):
    doctors = DoctorProfile.objects.all()[:6]
    latest_posts = Post.objects.order_by('-date')[:3]
    departments = Department.objects.all()
    context = {
        'doctors': doctors,
        'departments': departments,
        'latest_posts': latest_posts
    }
    return render(request, 'hospital/home.html', context)


# # Department List Views
class DepartmentListView(ListView):
    queryset = Department.objects.all()[:6]
    template_name = "hospital/departments.html"

# Department Detail View
class DepartmentDetailView(DetailView):
    queryset = Department.objects.all()
    template_name = "hospital/department_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['departments'] = Department.objects.all()
        return context
