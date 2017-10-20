"""atnpr URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from main import views as main_views
from django.contrib import admin

urlpatterns = [
    url(r'^clarkers/', admin.site.urls),
    url(r'^$', main_views.home, name='home'),
    url(r'^about$', main_views.about, name='about'),
    url(r'^services$', main_views.services, name='services'),
    url(r'^contact$', main_views.contact, name='contact'),
    url(r'^process$', main_views.process, name='process'),
    url(r'^blog$', main_views.blog, name='blog'),
    url(r'^thanks$', main_views.thanks, name='thanks'),
    url(r'^nope$', main_views.nope, name='nope'),
]
