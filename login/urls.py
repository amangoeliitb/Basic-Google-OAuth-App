from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^account/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^account/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$',
        'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT}),
]
