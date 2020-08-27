import uuid
import requests
import json
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import HttpResponse, render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from ProductApp.models import ProductOptions, Products
from ProductApp.helpers import (
    loadProductDetails,
    loadProductOptionDetails, validateObject,
    success_code, error_code
)

from rest_framework import serializers

product_keys = ['name', 'description', 'price', 'deliveryPrice']
product_options_keys = ['name', 'description']

class productDetails(APIView):
    '''
        - This view will get list of all products from DB
        - This view will save new product to DB
        - Methods - GET, POST
    '''

    def get(self, request, format = None):
        try:
            # When url consists more than one query parameters 
            if len(request.GET) > 1:
                raise Exception(error_code(6))
            if not request.GET:
                querySet = Products.objects.filter()
            else:
                resquested_name = request.GET['name']
                querySet = Products.objects.filter(name__contains=resquested_name)
                if not querySet:
                    raise Exception(error_code(8))
            
            response_items = loadProductDetails(self, querySet)
            
            return Response(response_items, status.HTTP_200_OK, content_type='application/json')

        except Exception as e:
            return Response({'Error' : str(e)}, status.HTTP_400_BAD_REQUEST, content_type='application/json')

    def post(self, request, format = None):
        try:
            data = request.data
            # validate the inputs
            is_valid = validateObject(
                validKeys = product_keys,
                data = data,
                check_all=True
            )

            if not is_valid:
                raise Exception(error_code(1))

            data['id'] = str(uuid.uuid4())

            prod = Products(
                id = data.get('id'),
                name = data.get('name'),
                description = data.get('description'),
                price = data.get('price'),
                deliveryPrice = data.get('deliveryPrice')
            )
 
            prod.save()

            return Response({ 'Message': success_code(1)}, status.HTTP_201_CREATED, content_type='application/json')

        except Exception as e:
            return Response({'Error' : str(e)}, status.HTTP_400_BAD_REQUEST, content_type='application/json')

        

class getProductById(APIView):
    '''
        - This view will get product by ID
        - This view will update product by ID
        - This view will delete product by ID
        - Methods - GET, PUT, DELETE
    '''

    def get(self, request, id, format = None):
        try:
            querySet = Products.objects.filter(id=id)

            if not querySet:
                raise Exception(error_code(7))

            response_items = loadProductDetails(self, querySet)

            return Response(response_items, status.HTTP_200_OK, content_type='application/json')

        except Exception as e:
            return Response({'Error' : str(e) }, status.HTTP_404_NOT_FOUND, content_type='application/json')
    
        
    
    def put(self, request, id, format = None):
        try:
            querySet = Products.objects.filter(id=id)
            
            if not querySet:
                raise Exception(error_code(5))
            data = request.data
            is_valid = validateObject(
                validKeys = product_keys,
                data = data
            )
            if not is_valid:
                raise Exception(error_code(2))

            prod = querySet[0]
            
            prod.name = data.get('name')
            prod.description = data.get('description')
            prod.price = data.get('price')
            prod.deliveryPrice = data.get('deliveryPrice')
            prod.save()

            return Response({ 'Message': success_code(2)}, status.HTTP_200_OK, content_type='application/json')

        except Exception as e:

            return Response({'Error' : str(e)}, status.HTTP_400_BAD_REQUEST, content_type='application/json')

    def delete(self, request, id, format = None):
        try:
            isdeleted = Products.objects.filter(id=id).delete()
            if isdeleted[0] == 0:
                raise Exception(error_code(3))
            return Response({ 'Message': success_code(3)}, status.HTTP_200_OK, content_type='application/json')
        except Exception as e:
            return Response({'Error' : str(e)}, status.HTTP_400_BAD_REQUEST, content_type='application/json')




class getProductOptions(APIView):
    '''
        - This view will get product option by specific product
        - This will will save new product options for a specific product
        - Methods - GET, POST
    '''

    def get(self, request, id, format = None):
        try:
            querySet = ProductOptions.objects.filter(productId=id)

            if not querySet:
                raise Exception(error_code(7))
            response_items = loadProductOptionDetails(self, querySet)
            return Response(response_items, status.HTTP_200_OK, content_type = 'application/json')
        except Exception as e:
            return Response({'Error' : str(e)}, status.HTTP_400_BAD_REQUEST, content_type = 'application/json')

    def post(self, request, id, format = None):
        try:
            data = request.data

            is_valid = validateObject(
                validKeys = product_options_keys,
                data = data,
                check_all=True
            )

            if not is_valid:
                raise Exception(error_code(1))

            data['id'] = str(uuid.uuid4())

            prod = ProductOptions(
                id = data.get('id'),
                productId = id,
                name = data.get('name'),
                description = data.get('description')
            )
            prod.save()
            return Response({ 'Message': success_code(1)}, status.HTTP_201_CREATED, content_type='application/json')

        except Exception as e:

            return Response({'Error' : str(e)}, status.HTTP_400_BAD_REQUEST, content_type = 'application/json')



class getProductOptionsById(APIView):
    '''
        - This view will get product options for a specific profcut by ID
        - This view will update product options for a specific profcut by ID
        - This view will delete product options for a specific profcut by ID
        - Methods - GET, PUT, DELETE
    '''

    def get(self, request, prodId, optionId, format = None):
        try: 
            querySet = ProductOptions.objects.filter(id = optionId, productId = prodId)
            if not querySet:
                raise Exception(error_code(7))

            response_items = loadProductOptionDetails(self, querySet)
            return Response(response_items, status.HTTP_200_OK, content_type = 'application/json')
        except Exception as e:
            return Response({'Error' : str(e)}, status.HTTP_400_BAD_REQUEST, content_type = 'application/json')

    
    def put(self, request, prodId, optionId, format = None):
        try:
            querySet = ProductOptions.objects.filter(id = optionId, productId = prodId)
            if not querySet:
                raise Exception(error_code(5))
            
            data = request.data
            is_valid = validateObject(
                validKeys = product_options_keys,
                data = data
            )

            if not is_valid:
                raise Exception(error_code(2))

            prod = querySet[0]        
            
            prod.name = data.get('name')
            prod.description = data.get('description')
            prod.save()
            return Response({ 'Message': success_code(2)}, status.HTTP_200_OK, content_type='application/json')
        except Exception as e:
            return Response({'Error' : str(e)}, status.HTTP_400_BAD_REQUEST, content_type='application/json')


    def delete(self, request, prodId, optionId, format = None):
            try:
                isdeleted = ProductOptions.objects.filter(id=optionId, productId=prodId).delete()
                if isdeleted[0] == 0:
                    raise Exception(error_code(3))
                return Response({ 'Message': success_code(3)}, status.HTTP_200_OK, content_type='application/json')
            except Exception as e:
                return Response({'Error' : str(e)}, status.HTTP_400_BAD_REQUEST, content_type='application/json')
