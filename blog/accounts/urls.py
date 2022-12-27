from django.conf.urls import url
from .views import SignUpView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [
    url('login/', LoginView.as_view(), name='login'),
    url('signup/', SignUpView.as_view(), name='signup'),
    url(r'^password_change/$',
        PasswordChangeView.as_view(template_name='registration/password-change.html'),
        name='password_change'),
    url(r'^password_reset/$',
        PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset'),
    url(r'^password_reset_done/$',
        PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    url(r'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done/$',
        PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

]
