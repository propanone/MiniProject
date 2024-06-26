"""
URL configuration for lib_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import *
urlpatterns = [
    path('', home),
    path('home', home),
    path('readers',reader_tab),
    path('readers/add', save_reader),
    path('books', book_tab),
    #path('books/add', save_book),
    path('blog', blog),
    path('bag', bag),
    path('upload', upload_csv),
    path('chart', chart),

]
