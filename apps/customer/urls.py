from django.urls import path

from apps.customer.views import CustomerView

urlpatterns = [
    path("customer/<uuid>", CustomerView.as_view(), name="customer"),
]
