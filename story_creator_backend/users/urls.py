from django.urls import path
from .views import RegisterView, LoginView, user_detail
from rest_framework_simplejwt.views import TokenRefreshView  # Import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', user_detail, name='user_detail'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Add 
]