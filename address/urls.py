from django.contrib import admin
from django.urls import path


from .views import *

urlpatterns = [
    path('', AddressList.as_view()),
    path('addresspost/',AddressPost.as_view()),
    path('address/<int:pk>/', AddressDetail.as_view()),
    path('addresssearch/',AddressSearch.as_view()),
    path('addressupdate/<int:pk>/',AddressUpdate.as_view())
]
