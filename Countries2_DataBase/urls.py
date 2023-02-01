"""FirstDZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.main),
    path('country_list/<int:page_number>', views.all_countries),
    path('country_list/<str:page_number>', views.all_countries),
    path('languages/all', views.languages),
    path('<str:country>', views.country_page),
    path('letter/<str:letter>', views.countries_by_letter),
    path('language/<str:language>', views.language_one),
]
