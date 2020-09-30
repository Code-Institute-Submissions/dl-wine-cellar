from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wines, name='wines'),
    path('<int:wine_id>/', views.wine_detail, name='wine_detail'),
    path('add/', views.add_wine, name='add_wine'),
    path('edit/<int:wine_id>/', views.edit_wine, name='edit_wine'),
    path('delete/<int:wine_id>/', views.delete_wine, name='delete_wine'),
]