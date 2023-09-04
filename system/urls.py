from django.contrib import admin
from django.urls import include, path

from system.views import LandingPageView, AboutPageView, ContactPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing"),
    path('about', AboutPageView.as_view(), name="about"),
    path('contact', ContactPageView.as_view(), name="contact"),
]
