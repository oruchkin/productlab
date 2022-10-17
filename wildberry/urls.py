from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    
    path("product/", views.Product_api.as_view()),
]




