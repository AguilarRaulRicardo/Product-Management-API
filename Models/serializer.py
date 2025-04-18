from rest_framework import serializers
from .models import Product, Category, Brand, Review

class ProductSerializer(serializers.ModelSerializer):
    category =  serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all())
    brand = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Brand.objects.all())
    
    class Meta:
        model = Product
        fields = ['id','category', 'brand', 'name', 'description', 'image', 'price', 'stock', 'create_at', 'update_at']
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

class SearchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50,required = False )
    min_price = serializers.IntegerField(required = False)
    ma_price = serializers.IntegerField(required = False)
    category = serializers.IntegerField(required = False) 
    brand = serializers.IntegerField(required = False)
    #agregar luego el filtro por resenas

class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = Review
        fields = ['id','product', 'rating', 'comment', 'create_at', 'user_id']
        read_only_fields = ['id', 'create_at']
