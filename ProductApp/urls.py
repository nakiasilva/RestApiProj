from django.conf.urls import include, url
from ProductApp.views import productDetails, getProductById, getProductOptions, getProductOptionsById
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    url(r'^products$', productDetails.as_view(), name = 'products'),
    url(r'^products/(?P<id>[a-zA-Z0-9\-]+)$', getProductById.as_view(), name = 'products-by-id'),
    url(r'^products/(?P<id>[a-zA-Z0-9\-]+)/options$', getProductOptions.as_view(), name = 'productoptions'),
    url(r'^products/(?P<prodId>[a-zA-Z0-9\-]+)/options/(?P<optionId>[a-zA-Z0-9\-]+)$', getProductOptionsById.as_view(), name = 'productoptions-by-optionid'),

 
]


 