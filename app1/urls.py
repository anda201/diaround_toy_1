from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('create/', views.create, name='create'),
]
