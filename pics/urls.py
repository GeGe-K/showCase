from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search', views.search_photo, name='search_photo'),
    url(r'^photo/(\d+)', views.photo, name='photo'),
    url(r'category/(\d+)', views.filter_by_category, name='category'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
