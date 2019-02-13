from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.index, name='index'),
    path('legalnotice_en/', views.legalnotice_en, name='legalnotice_en'),
    path('legalnotice_de/', views.legalnotice_de, name='legalnotice_de'),
    path('privacy_en/', views.privacy_en, name='privacy_en'),
    path('privacy_de/', views.privacy_de, name='privacy_de'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('contact_error/', views.contact_error, name='contact_error'),
]

# favicon handling, see http://staticfiles.productiondjango.com/blog/failproof-favicons/
urlpatterns += [
    path('favicon.ico',
         RedirectView.as_view(
            url=staticfiles_storage.url('mainpage/favicon/favicon.ico'),
            permanent=False
         ),
         name="favicon",
    ),
]
