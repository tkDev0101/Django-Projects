from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),

    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
