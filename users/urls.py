from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_details'),
    path('signup/', views.user_signup, name='signup'),


    # path('doctorlogin', LoginView.as_view(template_name='hospital/doctor_login.html'))
]