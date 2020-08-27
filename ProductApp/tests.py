import json
import uuid
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import reverse, resolve
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, URLPatternsTestCase

from ProductApp.views import (getProductById, getProductOptions,
	getProductOptionsById, productDetails)

from .models import Products, ProductOptions


# Create your tests here.

class TestUrls(SimpleTestCase):
	
	'''
		This class will test Product and 
		ProductOptions endpoints
	'''

	def test_products_url(self):
		url = reverse('products')
		self.assertEqual(resolve(url).func.view_class, productDetails)

	def test_products_by_id_url(self):
		url = reverse('products-by-id', args= ['some-id'])
		self.assertEqual(resolve(url).func.view_class, getProductById)

	def test_productoptions_url(self):
		url = reverse('productoptions', args= ['some-id'])
		self.assertEqual(resolve(url).func.view_class, getProductOptions)

	def test_productoptions_by_optionid_url(self):
		url = reverse('productoptions-by-optionid', args= ['some-product-id','some-productoption-id'])
		self.assertEqual(resolve(url).func.view_class, getProductOptionsById)



class ProductFunctionality(APITestCase):

	'''
		This class will test Product endpoint reponses
		Test Methods - GET, POST, PUT, DELETE
	'''

	def test_save_product(self):

		data = {
			'name' : 'Table', 
			'description' : 'Dining table', 
			'price' : 420.00, 
			'deliveryPrice': 24.99
		}
		url = reverse('products')
		response = self.client.post(url, data, format = 'json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_get_product(self):
		self.test_save_product()
		url = reverse('products')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		data = json.loads(response.content)
		id = data.get('Items')[0].get('Id')
		return id

	def test_get_product_by_name(self):
		self.test_save_product()
		url = reverse('products')
		response = self.client.get(url, {'name': 'Table'})
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_product_by_id(self):
		id = self.test_get_product()
		url = reverse('products-by-id', kwargs = {'id': id})
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_delete_by_id(self):
		id = self.test_get_product()
		url = reverse('products-by-id', kwargs = {'id': id})
		response = self.client.delete(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_by_id(self):
		id = self.test_get_product()
		url = reverse('products-by-id', kwargs = {'id': id})
		data = {
			'name' : 'Table', 
			'description' : 'Coffee table', 
			'price' : 420.00, 
			'deliveryPrice': 24.99
		}
		response =  self.client.put(url, data)
		url = reverse('products')
		data = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)




class ProductOptionsFunctionality(APITestCase):

	'''
		This class will test ProductOptions endpoint reponses
		Test Methods - GET, POST, PUT, DELETE
	'''

	def test_save_productoption(self):
		data = {
			'name' : 'Brown', 
			'description' : 'Brown table', 
		}
		url = reverse('productoptions', kwargs = {'id': 'some-id'} )
		response = self.client.post(url, data, format = 'json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
	def test_get_productoption(self):
		self.test_save_productoption()
		url = reverse('productoptions', kwargs = {'id': 'some-id'} )
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		data = json.loads(response.content)
		id = data.get('Items')[0].get('Id')
		return id

	def test_get_productoption_by_id(self):
		id = self.test_get_productoption()
		url = reverse('productoptions-by-optionid', kwargs = {'prodId': 'some-id', 'optionId' : id })
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_delete_by_id(self):
		id = self.test_get_productoption()
		url = reverse('productoptions-by-optionid', kwargs = {'prodId': 'some-id','optionId' : id })
		response = self.client.delete(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_update_by_id(self):
		id = self.test_get_productoption()
		url = reverse('productoptions-by-optionid', kwargs = {'prodId': 'some-id','optionId' : id })
		data = {
			'name' : 'Small Table', 
			'description' : 'Coffee table', 

		}
		response =  self.client.put(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

