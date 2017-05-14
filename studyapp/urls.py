from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from article import urls
from django.contrib.auth import views
from django.conf.urls.static import static  # for media
from django.conf import settings  # for media
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^', include('article.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
