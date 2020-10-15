from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView, RegisterActivateView, UserDetailView, \
    UserChangeView, UserPasswordChangeView, UserPasswordResetEmailView, UserPasswordResetView
from api.views import product_list_view

app_name = 'api'

urlpatterns = [
    path('add/', product_list_view, name='add'),

]