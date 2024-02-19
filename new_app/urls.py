from django.urls import path

from new_app import views

urlpatterns = [
    path('details', views.employeeDetails, name="details"),
    path('empdetail/<int:id>/',views.employee_detail,name='employee_detail')
]
