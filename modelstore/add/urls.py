from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('show/',views.show),
    path('filter/',views.filter),
    path('report/',views.report),
    path('capture/',views.capture),
    path('recognize/',views.recognize),
    path('test/',views.test),
    # path('entry/',views.entry),
    path('entryfilter/',views.entryfilter),
    path('query/',views.query),
    path('transfer_data/',views.transfer_data),
]