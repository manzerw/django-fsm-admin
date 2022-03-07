from django.urls.conf import patterns, include, re_path
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    "",
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    re_path(r"^admin/", include(admin.site.urls)),
)
