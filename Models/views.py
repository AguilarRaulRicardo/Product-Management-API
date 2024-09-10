from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import ProductSerializer, CategorySerializer, BrandSerializer
from .models import Product, Category, Brand
# Create your views here.

#create
@api_view(["POST"])
def create_product(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        #product = Product.objects.create(
        #    name = serializer.data['name'],
        #    description = serializer.data['description'],
        #    price = serializer.data['price'],
        #    stock = serializer.data['stock'],   
        #)
        #category = Category.objects.get(serializer.data['category'])
        #brand = Brand.objects.get(serializer.data['brand'])
        #product.category.add(category)
        #product.brand.add(brand)

        return Response({'product': serializer.data}, status = status.HTTP_201_CREATED)
    
    return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST) 

@api_view(["POST"])
def create_category(request):
    serializer = CategorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        #   Category.objects.create(name = serializer.data['name'])
        
        return Response({'category': serializer.data}, status = status.HTTP_201_CREATED)
    
    return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST) 

@api_view(["POST"])
def create_brand(request):
    serializer = BrandSerializer(data = request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        #Brand.objects.create(name = serializer.data['name'])
        
        return Response({'category': serializer.data}, status = status.HTTP_201_CREATED)
    
    return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST) 

#  list
@api_view(["GET"]) 
def list_product(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True) 
    return Response({'product': serializer.data}, status = status.HTTP_200_OK)

@api_view(["GET"]) 
def list_brand(request):
    brand = Brand.objects.all()
    serializer = BrandSerializer(brand, many = True) 
    return Response({'product': serializer.data}, status = status.HTTP_200_OK)

@api_view(["GET"]) 
def list_category(request):
    category = Category.objects.all()
    serializer = BrandSerializer(category, many = True) 
    return Response({'product': serializer.data}, status = status.HTTP_200_OK)

#update
@api_view(["PATCH"])
def update_product(request, pk):
    product = Product.objects.get(id = pk) 
    serializer = ProductSerializer(product, data = request.data, partial = True)
    if serializer.is_valid():
        serializer.save()

        return Response({"product": serializer.data}, status= status.HTTP_200_OK)
    
    return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["PATCH"])
def update_category(request, pk):
    category = Category.objects.get(id = pk) 
    serializer = CategorySerializer(category, data = request.data, partial = True)
    if serializer.is_valid():
        serializer.save()

        return Response({"category": serializer.data}, status= status.HTTP_200_OK)
    
    return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def update_brand(request, pk):
    brand = Brand.objects.get(id = pk) 
    serializer = BrandSerializer(brand, data = request.data, partial = True)
    if serializer.is_valid():
        serializer.save()

        return Response({"brand": serializer.data}, status= status.HTTP_200_OK)
    
    return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

#DELETE

@api_view(['DELETE'])
def delete_product(request, pk):
    product = Product.objects.get(id = pk)

    #agregar el token de autorizacion 
    product.delete()
    return Response({"Delete": "OK"}, status = status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_brand(request, pk):
    brand = Brand.objects.get(id = pk)

    #agregar el token de autorizacion 
    brand.delete()
    return Response({"Delete": "OK"}, status = status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_Category(request, pk):
    category = Category.objects.get(id = pk)

    #agregar el token de autorizacion 
    category.delete()
    return Response({"Delete": "OK"}, status = status.HTTP_200_OK)