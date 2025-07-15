from django.urls import path
from .views import ProgramView

urlpatterns = [
    path('programs/', ProgramView.as_view(), name='programs')
]