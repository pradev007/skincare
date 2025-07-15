from django.urls import path
from .views import HeadingViews

urlpatterns = [
    path('heading/', HeadingViews.as_view(),name="heading"),
]