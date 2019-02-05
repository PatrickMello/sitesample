"""sitesample URL Configuration

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
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]


# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        path('media/<str:path>', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    # ] + staticfiles_urlpatterns() + urlpatterns
        path('static/<str:path>', serve,
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    ] + urlpatterns
    pass
