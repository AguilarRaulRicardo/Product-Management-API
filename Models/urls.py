from django.urls import path
from . import views

urlpatterns = [
    #create
    path('create_category', views.create_category),
    path('create_product', views.create_product),
    path('create_brand', views.create_brand),
    #read
    path('list_product', views.list_product),
    path('list_brand', views.list_brand),
    path('list_category', views.list_category),
    #update
    path('update_product/<int:pk>', views.update_product),
    path('update_category/<int:pk>', views.update_category),
    path('update_brand/<int:pk>', views.update_brand),
    #delete
    path('delete_product/<int:pk>', views.delete_product),
    path('delete_brand/<int:pk>', views.delete_brand),
    path('delete_category/<int:pk>', views.delete_Category),
]