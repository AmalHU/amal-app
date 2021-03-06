from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('customers', views.customer_list),
    path('customers/<pk>', views.customer_detail),
    path('sp', views.serviceproviders_list),
    path('sp/<pk>', views.serviceproviders_detail),
]