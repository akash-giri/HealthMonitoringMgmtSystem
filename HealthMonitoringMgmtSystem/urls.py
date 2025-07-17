"""HealthMonitoringMgmtSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from healthapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('user_login/', user_login, name="user_login"),
    path('admin_login/', admin_login, name="admin_login"),
    path('change_password/', change_password, name="change_password"),
    path('user_change_password/', user_change_password, name="user_change_password"),
    path('logout_admin/', logout_admin, name="logout_admin"),
    path('logout_user/', logout_user, name="logout_user"),
    path('user_register/', user_register, name="user_register"),
    path('user_profile/', user_profile, name="user_profile"),
    path('view_reg_user/', view_reg_user, name="view_reg_user"),
    path('user_dashboard/', user_dashboard, name="user_dashboard"),
    path('dashboard/', dashboard, name="dashboard"),
    path('admin_bp_report/', admin_bp_report, name="admin_bp_report"),
    path('admin_bs_report/', admin_bs_report, name="admin_bs_report"),
    path('admin_bt_report/', admin_bt_report, name="admin_bt_report"),
    path('blood_pressure_report/', blood_pressure_report, name="blood_pressure_report"),
    path('blood_sugar_report/', blood_sugar_report, name="blood_sugar_report"),
    path('body_temprature_report/', body_temprature_report, name="body_temprature_report"),
    path('add_member/', add_member, name="add_member"),
    path('manage_member/', manage_member, name="manage_member"),
    path('manage_testing_range/', manage_testing_range, name="manage_testing_range"),
    path('manage_blood_pressure/', manage_blood_pressure, name="manage_blood_pressure"),
    path('manage_blood_sugar/', manage_blood_sugar, name="manage_blood_sugar"),
    path('manage_body_temprature/', manage_body_temprature, name="manage_body_temprature"),
    path('add_testing_range/', add_testing_range, name="add_testing_range"),
    path('add_blood_pressure/', add_blood_pressure, name="add_blood_pressure"),
    path('add_blood_sugar/', add_blood_sugar, name="add_blood_sugar"),
    path('add_body_temprature/', add_body_temprature, name="add_body_temprature"),
    path('edit_member/<int:pid>/', edit_member, name="edit_member"),
    path('delete_member/<int:pid>/', delete_member, name="delete_member"),
    path('delete_blood_sugar/<int:pid>/', delete_blood_sugar, name="delete_blood_sugar"),
    path('delete_blood_pressure/<int:pid>/', delete_blood_pressure, name="delete_blood_pressure"),
    path('delete_body_temprature/<int:pid>/', delete_body_temprature, name="delete_body_temprature"),
    path('delete_testing_range/<int:pid>/', delete_testing_range, name="delete_testing_range"),
    path('update_testing_range/<int:pid>/', update_testing_range, name="update_testing_range"),
    path('history_blood_pressure/<int:pid>/', history_blood_pressure, name="history_blood_pressure"),
    path('history_blood_sugar/<int:pid>/', history_blood_sugar, name="history_blood_sugar"),
    path('history_body_temprature/<int:pid>/', history_body_temprature, name="history_body_temprature"),
    path('fullname/', fullname, name="fullname"),
]
