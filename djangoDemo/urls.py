from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.static import serve

from blog import views
from . import settings

urlpatterns = [url(r'^admin/', admin.site.urls),
               url(r'^$', views.IndexView.as_view(), name='index'),
               url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
               url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
               path(r'about.html', views.AboutMeView.as_view(), name='about'),
               path(r'index.html', views.FirstPage.as_view(), name='first')]
