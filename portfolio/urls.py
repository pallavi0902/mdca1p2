from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views

app_name = 'portfolio'
urlpatterns = [


    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('investment_list', views.investment_list, name='investment_list'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),
    path('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path('investment/create/', views.investment_new, name='investment_new'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    path('mutualfund_list', views.mutualfund_list, name='mutualfund_list'),
    path('mutualfund/create/', views.mutualfund_new, name='mutualfund_new'),
    path('mutualfund/<int:pk>/edit/', views.mutualfund_edit, name='mutualfund_edit'),
    path('mutualfund/<int:pk>/delete/', views.mutualfund_delete, name='mutualfund_delete'),
    url(r'^customers_json/', views.CustomerList.as_view()),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^password-reset/complete/$',auth_views.password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^reset/password_reset/$', auth_views.password_reset, name='password_reset_1'),
    url(r'^password-reset/done/$',auth_views.password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm,
            {'template_name': 'registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^password-reset/complete/$',auth_views.password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
