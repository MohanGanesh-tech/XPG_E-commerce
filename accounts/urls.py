from django.urls import path, URLPattern
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include

urlpatterns = [
    path('',views.index,name='index'),
    path('registers',views.registers,name='registers'),
    path('login',views.login,name='login'),

    # #Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), 
    #     name='password_change_done'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), 
    #     name='password_change'),

    # path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),
    #  name='password_reset_done'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    #  name='password_reset_complete'),


    # # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),



    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), 
        name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),

   

    

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

    

    

]