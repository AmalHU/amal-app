from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


# Create your views here.

  
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Add Customer': '/customer',
        'Update': '/customer/<pk>',
        'Delete': '/customer/<pk>'
    }
  
    return Response(api_urls)

# Customer API GET, POST, PUT, DELETE

@api_view(['GET', 'POST', 'DELETE'])
def customer_list(request):
    # GET list of Customers, POST a new Customer, DELETE all Customers

    if request.method == 'GET':
        customers = Customer.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            customers = customers.filter(title__icontains=title)
        
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Customer.objects.all().delete()
        return JsonResponse({'message': '{} Customers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
    # find customer by pk (id)
    try: 
        customer = Customer.objects.get(pk=pk) 
    except Customer.DoesNotExist: 
        return JsonResponse({'message': 'The customer does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE Customer
    # ... customer = Customer.objects.get(pk=pk)
 
    if request.method == 'GET': 
        customer_serializer = CustomerSerializer(customer) 
        return JsonResponse(customer_serializer.data)
    
    elif request.method == 'PUT': 
        customer_data = JSONParser().parse(request) 
        customer_serializer = CustomerSerializer(customer, data=customer_data) 
        if customer_serializer.is_valid(): 
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        customer.delete() 
        return JsonResponse({'message': 'Customer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

    
        
@api_view(['GET'])
def customer_list_published(request):
    # GET all published Customer

    customers = Customer.objects.filter(published=True)
        
    if request.method == 'GET': 
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)

# Service Providers API GET, POST, PUT, DELETE

@api_view(['GET', 'POST', 'DELETE'])
def serviceproviders_list(request):
    # GET list of ServiceProviders, POST a new ServiceProvider, DELETE all ServiceProviders

    if request.method == 'GET':
        serviceproviders = ServiceProviders.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            serviceproviders = serviceproviders.filter(title__icontains=title)
        
        serviceproviders_serializer = ServiceProviderSerializer(serviceproviders, many=True)
        return JsonResponse(serviceproviders_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        serviceproviders_data = JSONParser().parse(request)
        serviceproviders_serializer = ServiceProviderSerializer(data=serviceproviders_data)
        if serviceproviders_serializer.is_valid():
            serviceproviders_serializer.save()
            return JsonResponse(serviceproviders_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serviceproviders_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = ServiceProviders.objects.all().delete()
        return JsonResponse({'message': '{} Service Providers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def serviceproviders_detail(request, pk):
    # find serviceproviders by pk (id)
    try: 
        serviceproviders = ServiceProviders.objects.get(pk=pk) 
    except ServiceProviders.DoesNotExist: 
        return JsonResponse({'message': 'The Service Provider does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE serviceproviders
    # ... serviceproviders = ServiceProviders.objects.get(pk=pk)
 
    if request.method == 'GET': 
        serviceproviders_serializer = ServiceProviderSerializer(serviceproviders) 
        return JsonResponse(serviceproviders_serializer.data)
    
    elif request.method == 'PUT': 
        serviceproviders_data = JSONParser().parse(request) 
        serviceproviders_serializer = ServiceProviderSerializer(serviceproviders, data=serviceproviders_data) 
        if serviceproviders_serializer.is_valid(): 
            serviceproviders_serializer.save() 
            return JsonResponse(serviceproviders_serializer.data) 
        return JsonResponse(serviceproviders_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        ServiceProviders.delete() 
        return JsonResponse({'message': 'Service Provider was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
def serviceproviders_list_published(request):
    # GET all published ServiceProviders

    serviceproviders = ServiceProviders.objects.filter(published=True)
        
    if request.method == 'GET': 
        serviceproviders_serializer = ServiceProviderSerializer(serviceproviders, many=True)
        return JsonResponse(serviceproviders_serializer.data, safe=False)