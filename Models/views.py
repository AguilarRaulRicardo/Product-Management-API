from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


from .serializer import ProductSerializer, CategorySerializer, BrandSerializer, SearchSerializer, ReviewSerializer
from .models import Product, Category, Brand, Review
# Create your views here.

def validate_user(token):
    url = 'http://127.0.0.1:8001/validate_user'
    headers = {
        'Content-Type': 'application/json',
    }
    data = {'token': token}
    response = requests.get(url, json=data, headers=headers)
    if response.status_code == 200:
        user_id = list(response.json().values())[0]
        return True, user_id 
    else:
        return False, None

def validate_staff(token):
    url = 'http://127.0.0.1:8001/validate_staff'
    headers = {
        'Content-Type': 'application/json',
    }   
    data = {'token': token}
    response = requests.get(url, json=data, headers=headers)
    print(list(response.json().values()))
    if response.status_code == 200:
        user_id = list(response.json().values())[0]
        return True, user_id
    else:
        return False, None
#create
@api_view(["POST"])
def create_product(request): 
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        staff, admin = validate_staff(token)
        if staff:
            serializer = ProductSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'product': serializer.data}, status = status.HTTP_201_CREATED)
            
            return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)  
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])
def create_category(request):
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        staff, admin = validate_staff(token)
        if staff:
            print(request.data)
            serializer = CategorySerializer(data = request.data)
            if serializer.is_valid():
                serializer.save() 
                return Response({'category': serializer.data}, status = status.HTTP_201_CREATED)
            
            return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST) 
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def create_brand(request):
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        staff, admin = validate_staff(token)
        if staff:
            serializer = BrandSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response({'category': serializer.data}, status = status.HTTP_201_CREATED)
            
            return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST) 
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def create_review(request):
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        token, user = validate_user(token)
        user = {'user_id': user}
        data = request.data
        data = data.update(user)
        if token: 
            serializer = ReviewSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Review": serializer.data}, status= status.HTTP_201_CREATED)
            
            return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST) 
        
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)
#  list
@api_view(["GET"]) 
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True) 
    return Response({'products': serializer.data}, status = status.HTTP_200_OK)

@api_view(["GET"]) 
def list_product(request, id):
    try:
        product = Product.objects.get(id = id)
        serializer = ProductSerializer(product)
        return Response({'product': serializer.data}, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({'product': "product does not exist"}, status=status.HTTP_404_NOT_FOUND)
        


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

@api_view(["GET"])
def list_reviews(request, pk):
    review = Review.objects.filter(product = pk)
    serializer = ReviewSerializer(review, many = True)
    return Response({'review': serializer.data}, status = status.HTTP_200_OK)

#update
@api_view(["PATCH"])
def update_product(request, pk):
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        staff, admin = validate_staff(token)
        if staff:
            product = Product.objects.get(id = pk) 
            serializer = ProductSerializer(product, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()

                return Response({"product": serializer.data}, status= status.HTTP_200_OK)          
            return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)

@api_view(["PATCH"])
def update_category(request, pk):
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        staff, admin = validate_staff(token)
        if staff:
            category = Category.objects.get(id = pk) 
            serializer = CategorySerializer(category, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()

                return Response({"category": serializer.data}, status= status.HTTP_200_OK)
            
            return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def stock_decrement(request, pk):
    try:
        token = request.headers.get('Authorization').split(" ")[1] 
        key, users =validate_user(token)
        if key:
            product = Product.objects.get(id = pk)
            product.Stock = product.Stock - request.data["quantity"] 
            print(product.Stock)
            serializer = ProductSerializer(product, data = {"Stock":product.Stock}, partial = True)
            if serializer.is_valid():
                serializer.save()

                return Response({"Stock updated": serializer.data}, status= status.HTTP_200_OK)

            return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)

@api_view(["PATCH"])
def update_brand(request, pk):
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        staff, admin = validate_staff(token)
        if staff:
            brand = Brand.objects.get(id = pk) 
            serializer = BrandSerializer(brand, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()

                return Response({"brand": serializer.data}, status= status.HTTP_200_OK)
            
            return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)
@api_view(["PATCH"])
def update_review(request, pk):
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        token, user = validate_user(token)
        if token:
            try:
                review = Review.objects.get(id = pk, user_id = user)     
                
                serializer = ReviewSerializer(review, data = request.data, partial = True)
                if serializer.is_valid():
                    serializer.save()

                    return Response({"review": serializer.data}, status= status.HTTP_200_OK)
            
                return Response({"error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
            except Review.DoesNotExist:
                return Response({"Error": "Review or user not found"}, status= status.HTTP_404_NOT_FOUND)

        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)

    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)

#DELETE

@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        staff, admin = validate_staff(token)
        if staff:
            product = Product.objects.get(id = pk)
            name = product.name
            id = product.id
            product.delete()
            return Response({"Deleted Product id": [name, id] }, status = status.HTTP_200_OK)
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_brand(request, pk):
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        staff, admin = validate_staff(token)
        if staff:
            brand = Brand.objects.get(id = pk)
            name = brand.name
            id = brand.id
            brand.delete()
            return Response({"Deleted Brand": [name, id]}, status = status.HTTP_200_OK)
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_Category(request, pk):
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        staff, admin = validate_staff(token)
        if staff:
            category = Category.objects.get(id = pk)
            name = category.name
            id = category.id
            category.delete()
            return Response({"Deleted Category": [name, id]}, status = status.HTTP_200_OK)
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def delete_review(request, pk):
    try:
        token = request.headers.get('Authorization').split(" ")[1]
        staff, admin = validate_staff(token)
        token, user = validate_user(token) 
        if staff:
            try:
                review = Review.objects.get(id = pk)
                review.delete()
                name = review.name
                id = review.id
                return Response({"Deleted review": [name, id]}, status = status.HTTP_200_OK)
            except Review.DoesNotExist:
                return Response({"Error": "review not found"}, status=status.HTTP_404_NOT_FOUND)
        elif token: 
            try:
                review = Review.objects.get(id = pk, user_id = user)

                name = review.name
                id = review.id
                review.delete()
                return Response({"Deleted review": [name, id]}, status = status.HTTP_200_OK)
            except Review.DoesNotExist:
                return Response({"Error": "review or user not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"Error": "unauthorized"}, status= status.HTTP_401_UNAUTHORIZED)

    except IndexError:
        return Response({"Error": "Missing Token Error"}, status= status.HTTP_400_BAD_REQUEST)
    except AttributeError: 
        return Response({"Error": "Missing Authorization Error"}, status= status.HTTP_400_BAD_REQUEST)
    

#search

@api_view(['GET'])
def search_product(request):
    serializer = SearchSerializer(data = request.data, partial = True)
    if serializer.is_valid():
        
        datos = serializer.data.keys()
        
        if "name" in datos:
            product = Product.objects.filter(name__contains = serializer.data["name"])
        if "max_price" in datos and "min_price" in datos:
            product = Product.objects.filter(price__lt = serializer.data["max_price"],price__gt = serializer.data["min_price"] )
        if "category" in datos:
            product  = Product.objects.filter(category__exact = serializer.data["category"])
        
        if "brand" in datos:
            product = Product.objects.filter(brand__exact = serializer.data["brand"])
            
        serializer = ProductSerializer(product, many = True)

        #agregar filtrado por resenias 

        return Response({"Product": serializer.data}, status= status.HTTP_200_OK)

    return Response({"Error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

