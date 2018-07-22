from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from django.contrib.auth import views as auth_views
from portfolio.views import login_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^register/', register_view, name='register'),

    # restore password urls
    url(r'^reset/password_reset/$', auth_views.password_reset, name='password_reset_1'),
    url(r'^password-reset/done/$',auth_views.password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm,
            {'template_name': 'registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^password-reset/complete/$',auth_views.password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),
]
