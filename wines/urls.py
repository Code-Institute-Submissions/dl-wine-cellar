from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wines, name='wines'),
    path('<int:wine_id>/', views.wine_detail, name='wine_detail'),
    path('add/', views.add_wine, name='add_wine'),
]