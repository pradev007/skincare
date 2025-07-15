from django.urls import path
from .views import ServicesView

urlpatterns = [
    path('services/', ServicesView.as_view(),name='Services')
]