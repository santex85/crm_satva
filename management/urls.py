from django.urls import path
from management import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
]
