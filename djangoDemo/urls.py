from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.static import serve

from blog.views import IndexView
from . import view, search, search2, settings

urlpatterns = [url(r'^admin/', admin.site.urls),
               url(r'^$', IndexView.as_view(), name='index'),
               url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
               url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
               path('hello/', view.hello),
               path('search', search.search),
               path('search_form', search.search_form),
               path('search_post', search2.search_post)]
