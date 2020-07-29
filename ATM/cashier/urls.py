from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cashier-home'),
    path('result', views.result, name='cashier-result'),
    path('transactions', views.transactions, name='cashier-transactions')
]