from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinancialRecordViewSet

router = DefaultRouter()
router.register(r'records', FinancialRecordViewSet, basename='record')

urlpatterns = [
    path('', include(router.urls)),
]
