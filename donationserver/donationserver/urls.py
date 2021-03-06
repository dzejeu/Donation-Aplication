"""donationserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^$', views.login_view, name='start'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home_view, name='home'),
    url(r'^gathering/', views.gathering, name='gathering'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^logout/', views.logout_user, name='logout'),
    url(r'^pass/', views.change_pass, name='pass'),
    url(r'^creategathering/', views.create_gathering, name='creategathering'),
    url(r'^register/', views.register_user, name='register'),
    url(r'^donateothers/', views.query_gatherings, name='donate'),
    url(r'^paybtc/', views.paybtc, name='paybtc'),
    url(r'^transaction/', views.finalize_payment, name='transaction'),
]
