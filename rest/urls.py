from django.urls import path

from car import views

urlpatterns = [
    path('cars', views.ListCreateCarView.as_view()),
    path('cars/<int:pk>', views.UpdateDeleteCarView.as_view()),
]
