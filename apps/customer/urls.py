from django.urls import path

from apps.customer import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("customer", views.CustomerView.as_view(), name="customer"),
]
