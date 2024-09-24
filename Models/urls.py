from django.urls import path
from . import views

urlpatterns = [
    #create
    path('create_category', views.create_category),
    path('create_product', views.create_product),
    path('create_brand', views.create_brand),
    path('create_review', views.create_review),
    
    #read
    path('list_product', views.list_product),
    path('list_brand', views.list_brand),
    path('list_category', views.list_category),
    path('list_review/<int:pk>', views.list_reviews),
    #update
    path('update_product/<int:pk>', views.update_product),
    path('update_category/<int:pk>', views.update_category),
    path('update_brand/<int:pk>', views.update_brand),
    path('update_review/<int:pk>', views.update_review),
    #delete
    path('delete_product/<int:pk>', views.delete_product),
    path('delete_brand/<int:pk>', views.delete_brand),
    path('delete_category/<int:pk>', views.delete_Category),
    path('delete_review/<int:pk>', views.delete_review),
    #search
    path('search_product', views.search_product),
]