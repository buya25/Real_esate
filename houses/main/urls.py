from django.urls import path
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.home, name='home'),
    # URL pattern for accessing titles under a category
    path('categories/', views.category_list_view, name='category-list'),
    path('category/<slug:category_slug>/', views.category_detail_view, name='category-detail'),
]
