from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('show/',views.show),
    path('filter/',views.filter),
    path('report/',views.report),
    path('capture/',views.capture),
]