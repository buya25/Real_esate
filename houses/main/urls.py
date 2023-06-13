from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.home, name='home'),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Add the following line to serve media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)