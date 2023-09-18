from django.urls import path
from TVapp import views

urlpatterns = [
    path('company', views.CompanyApi),
    path('company/<int:id>', views.CompanyApi),

     path('employee', views.EmployeeApi),
    path('employee/<int:id>', views.EmployeeApi),
]