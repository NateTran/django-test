"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, info_view, context_view
from testapp.views import testapp_detail_view, testapp_create_view, testapp_create_view_django

urlpatterns = [
    path('', home_view, name='home'),
    path('info/', info_view),
    path('context/', context_view),
    path('details/', testapp_detail_view),
    path('premade/', testapp_create_view),
    path('create/', testapp_create_view_django),
    path('admin/', admin.site.urls),
]
