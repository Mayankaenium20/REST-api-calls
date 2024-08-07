from django.urls import path, include
from .views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

#router: setting up a router for the app to manage the app 

router = routers.DefaultRouter()
router.register(r'company_', CompanyViewSet)                   #this will allow us the to perform the get, post, put, and delete operations via the company viewset without explicitely specifying the url endpoints in the urls.py
router.register(r'employee_', EmployeeViewSet)                                                               #'company_' is how we'll access the company method operations via the url: .../api/v1/company_

urlpatterns = [
    path('', include(router.urls)), 
    path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
]