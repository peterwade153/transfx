from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('accounts', views.AccountView, basename='accounts')
router.register('transfers', views.TransferView, basename='transfers')
router.register('account-balance', views.AccountBalanceView, basename='account-balance')
router.register('account-transactions', views.AccountTransactionsView, basename='account-transactions')

urlpatterns = [
    path('', include(router.urls))
]
