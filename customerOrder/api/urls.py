from rest_framework.urls import path
from . import views


urlpatterns = [
    path('customer/', views.CustomerListCreateAPIView.as_view()),
    path('order/', views.OrderListCreateAPIView.as_view()),
]