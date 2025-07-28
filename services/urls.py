from django.urls import path
from .views import ServicesListCreateView

urlpatterns = [
    path('services/', ServicesListCreateView.as_view(),name='Services'),
    # path('services/<int:pk>', ServicesListCreateView.as_view , name="services details")
]