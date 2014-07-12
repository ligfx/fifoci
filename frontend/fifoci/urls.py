from django.conf import settings
from django.conf.urls import patterns, include, static, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fifoci.views.home', name='home'),
    url(r'^dff/$', 'fifoci.views.dffs_to_test'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL,
                                 document_root=settings.MEDIA_ROOT)
