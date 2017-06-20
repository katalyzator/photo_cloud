"""cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, patterns, include
from django.conf.urls.static import static
from django.contrib import admin
from tastypie.api import Api
from upload_app.api import *

from photo_cloud import settings

v1 = Api(api_name='v1')
v1.register(FolderResource())
v1.register(SubfolderResource())
v1.register(FolderImageResource())
urlpatterns = patterns('',
                       url(r'^jet/', include('jet.urls', 'jet')),
                       url(r'^admin/', admin.site.urls),
                       url(r'^api/', include(v1.urls)),
                       url(r'^get_password', 'upload_app.views.get_password', name='get_password'),
                       )
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
