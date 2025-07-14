# accounts/urls.py
from django.urls import path
from .views import RegisterView, CustomLoginView, LogoutView, VendorDashboardView, UserProfileView, AdminPanelView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('vendor/dashboard/', VendorDashboardView.as_view(), name='vendor_dashboard'),
    path('user/profile/', UserProfileView.as_view(), name='user_profile'),
    path('admin/panel/', AdminPanelView.as_view(), name='admin_panel'),
]