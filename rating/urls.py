from django.urls import path
from .views import RatingView

urlpatterns = [
    path('rating/', RatingView.as_view(),name="rating"),
]