from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register,name='register'),
    #path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('login', views.login,name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('feedback', views.feedback,name='feedback'),
    path('export-csv', views.export_csv,name='export-csv'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    path('verify/<auth_token>', views.verify,name='verify'),
]
