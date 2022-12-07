from django.urls import path
from . import views


urlpatterns = [
    path('', views.products_list),
    path('<int:pk>/', views.products_item) #Passes the pk as an integer through the path.



]
