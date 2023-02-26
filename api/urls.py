
from django.urls import path
from api import views


urlpatterns = [
    path('api',views.shop_list), 
    path('api/<int:pk>/',views.shop_detail),
]
