from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category_detail_view, name='category-det'),
    path('agent/', views.agent_page, name='agent'),
    path('blog/', views.blog_page, name='blog'),
    path('blog/<slug:slug>/', views.properties_details, name='properties_details'),
    path('contact/', views.contact_page, name='contact'),
    path('submit_comment/<int:blog_id>/', views.submit_comment, name='submit_comment'),
    path('submit_comment/<slug:slug>/', views.submit_comment_main, name='submit_comment'),
    path('reply/<int:comment_id>/', views.reply_to_comment, name='reply_to_comment'),
    path('contact/', views.contact_form, name='contact_form'),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Add the following line to serve media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
