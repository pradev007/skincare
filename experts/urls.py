from django.urls import path
from .views import ExpertListCreateApi, ExpertRetrieveUpdateDeleteApi

urlpatterns = [
    path('experts/', ExpertListCreateApi.as_view(), name='expert'),
    path('experts/<int:pk>/', ExpertRetrieveUpdateDeleteApi.as_view(), name= 'expert-detail'),
]