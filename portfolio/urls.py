"""portfolio URL Configuration

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
from django.contrib import admin
from django.urls import path
import jobs.views # Add this line to import the jobs app views
from django.conf import settings # Add this line to import the settings module
from django.conf.urls.static import static # Add this line to import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.homepage, name='homepage'), # Add this line to add the homepage/landing page view
    path('jobs/<int:job_id>', jobs.views.detail, name='detail'), # Add this line to add the homepage/landing page view
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
