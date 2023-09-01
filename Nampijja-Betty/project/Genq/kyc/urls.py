from django.urls import path
from . import views
urlpatterns = [
    path('', views.base, name='base'),
    # path('', views.base, name='base'),
    path('form/', views.form, name='form'),
    path('success/', views.success, name='success'),
]
