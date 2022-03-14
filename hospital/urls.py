from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('departments/', views.DepartmentListView.as_view(), name='departments'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_details'),
]