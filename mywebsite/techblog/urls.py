from django.urls import path, re_path, include
from . import views
from wagtail.core import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls


urlpatterns = [
    path('', views.index, name='techblog_index'),
    path('search', views.searchIndex, name='techblog_search_index'),
    path('category', views.categoryIndex, name='techblog_category_index'),
    path('tag', views.tagIndex, name='techblog_tag_index'),
    re_path(r'^posts/', include(wagtail_urls)),
    re_path(r'^admin/', include(wagtailadmin_urls)),
]
