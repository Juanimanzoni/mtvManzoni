"""mvtManzoni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from AppFlia.views import cargo_fliar1, cargo_fliar2, cargo_fliar3, cargo_fliar_todos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familiar1/',cargo_fliar1),
    path('familiar2/',cargo_fliar2),
    path('familiar3/',cargo_fliar3),
    path('familiar todos/',cargo_fliar_todos),
]
