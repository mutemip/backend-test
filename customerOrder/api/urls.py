from django.urls import path
from . import views


urlpatterns = [
    path('customer/', views.CustomerListCreateAPIView.as_view()),
    path('order/', views.OrderListCreateAPIView.as_view()),
    # path('google/callback/', GoogleLoginApi.as_view(), name='callback'),
    # path('google/redirect/', GoogleLoginRedirectApi.as_view(), name='redirect'),
]
