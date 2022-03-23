from django.urls import path

from apps.customer import views
from apps.customer.API.api import api

urlpatterns = [
    path("api/", api.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("customer", views.CustomerView.as_view(), name="customer"),
]
