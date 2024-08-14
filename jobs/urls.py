from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
    path('post_job/', views.post_job, name='post_job'),
    path('success/', views.application_success, name='application_success'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
]
