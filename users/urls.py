from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_details'),
    path('signup/', views.user_signup, name='signup'),
    path('login_user/', views.user_login, name='user_login'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # <-- this one here

    path('add_country/', views.add_country, name='add_country'),
    path('add_city/', views.add_city, name='add_city'),
    path('add_profile/', views.doctor_create_view, name='add_profile'),



    # path('doctorlogin', LoginView.as_view(template_name='hospital/doctor_login.html'))
]