from django.urls import path
from . import views

app_name = 'hospital'

urlpatterns = [
    path('', views.home, name='hospital-home'),
    # path('', views.HomeView.as_view(), name='hospital-home'),
    path('departments/', views.DepartmentListView.as_view(), name='departments'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_details'),
]