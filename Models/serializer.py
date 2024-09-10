from rest_framework import serializers
from .models import Product, Category, Brand

class ProductSerializer(serializers.ModelSerializer):
    category =  serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all())
    brand = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Brand.objects.all())
    
    class Meta:
        model = Product
        fields = ['id','category', 'brand', 'name', 'description', 'price', 'Stock', 'create_at', 'update_at']
        read_only_fields = ['id', 'create_at', 'update_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']

class BrandSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Brand
        fields = ['id', 'name']
        read_only_fields = ['id']

#class ReviewSerializer(serializers.ModelSerializer):
#    class Meta:
#        m

