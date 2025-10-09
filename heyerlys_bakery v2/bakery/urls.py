from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('orders/', views.order, name='orders'),  # shows order form
    path('order_submit/', views.order_submit, name='order_submit'),  # handles POST
    path('confirmation/<int:order_id>/', views.confirmation, name='confirmation'),
    path('employee/', views.employee, name='employee'),
    path('complete_order/<int:order_id>/', views.complete_order, name='complete_order'),
]
