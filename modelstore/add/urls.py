from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.home, name='home'),
    path('show/', views.show, name='show'),
    path('filter/', views.filter, name='filter'),
    path('report/', views.report, name='report'),
    path('capture/', views.capture, name='capture'),
    path('recognize/', views.recognize, name='recognize'),
    path('test/', views.test, name='test'),
    path('entryfilter/', views.entryfilter, name='entryfilter'),
    path('query/', views.query, name='query'),
    path('transfer_data/', views.transfer_data, name='transfer_data'),
    path('index/', views.index, name='index'),
]