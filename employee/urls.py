from django.urls import path
from . import views

app_name = "employee"

urlpatterns = [
    path('dashboard/employee-profile/', views.employee_profile, name='employee-profile'),
    path('exp-save', views.exp_save, name="exp_save"),
    path('edu-save', views.edu_save, name="edu_save"),
    path('cer-save', views.cer_save, name="cer_save"),
    path('skl-save', views.skl_save, name="skl_save"),
    path('lng-save', views.lng_save, name="lng_save"),
    path('edu-delete', views.edu_delete, name="edu_delete"),
    path('exp-delete', views.exp_delete, name="exp_delete"),
    path('cer-delete', views.cer_delete, name="cer_delete"),
    path('skl-delete', views.skl_delete, name="skl_delete"),
    path('lng-delete', views.lng_delete, name="lng_delete"),
    path('edu-edit', views.edu_edit, name="edu_edit"),
    path('exp-edit', views.exp_edit, name="exp_edit"),
    path('cer-edit', views.cer_edit, name="cer_edit"),
    path('resume_create', views.resume_create, name="resume_create"),
    path('dashboard/employee/', views.employee_dashboard, name='employee-dashboard'),

]