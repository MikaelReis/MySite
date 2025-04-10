"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
=======
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
>>>>>>> a993f214c704b874056ff7b22412a018e1702d17
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
<<<<<<< HEAD
    2. Add a URL to urlpatterns:  path('blog_old/', include('blog_old.urls'))
=======
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
>>>>>>> a993f214c704b874056ff7b22412a018e1702d17
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('home/', include('blog_app.urls')),  # aponta pro app novo
=======
    path('home', include('blog.urls')),
>>>>>>> a993f214c704b874056ff7b22412a018e1702d17
]
