from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:code>/', views.qr_redirect_view, name='qr-redirect'),
    path('<slug:code>/details/', views.qr_detail_view, name='qr-detail'),

]