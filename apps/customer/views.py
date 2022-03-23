from django.shortcuts import render, redirect
from apps.customer import models
from apps.core.models import User
from django.views.generic import ListView, TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q


class IndexView(TemplateView):
    template_name = "index.html"
    context = {}

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("customer")
        else:
            return redirect("login")

    def post(self, *args, **kwargs):
        return redirect("index")


class LoginView(TemplateView):
    template_name = "customer/login.html"
    context = {}

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("customer")
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        try:
            email = self.request.POST.get("email")
            password = self.request.POST.get("password")
            if email and password:
                user = authenticate(email=email, password=password)
                if user is None:
                    raise Exception("Invalid User")
                login(self.request, user)
            return redirect("index")
        except Exception as e:
            return redirect("login", error=True)


class LogoutView(LoginRequiredMixin, RedirectView):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect("index")


class RegisterView(LoginRequiredMixin, TemplateView):
    template_name = "customer/register.html"
    context = {}

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        user_data = {
            "email": self.request.POST.get("email"),
            "first_name": self.request.POST.get("first_name"),
            "last_name": self.request.POST.get("last_name"),
            "birth": self.request.POST.get("birth"),
            "password": self.request.POST.get("password"),
        }
        user = User.objects.create_user(**user_data)
        user.save()
        address_list = [v for k, v in self.request.POST.items() if "address" in k and v]
        for current_address in address_list:
            address = models.Address.objects.create(user=user, address=current_address)
            address.save()
        phone_list = [v for k, v in self.request.POST.items() if "phone" in k and v]
        for current_phone in phone_list:
            phone = models.Phone.objects.create(user=user, number=current_phone)
            phone.save()
        return redirect("login")


class CustomerView(LoginRequiredMixin, TemplateView):
    template_name = "customer/customer.html"
    context = {
        "customer_list": User.objects.filter().order_by("id") 
    }

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            query = Q()
            query_string = self.request.GET.get("query")
            is_active = self.request.GET.get("is_active")
            if query_string is not None:
                query |= Q(email__icontains=query_string)
                query |= Q(first_name__icontains=query_string)
                query |= Q(last_name__icontains=query_string)
            if is_active is not None and is_active.isnumeric:
                query &= Q(is_active=int(is_active))
            customer_list = User.objects.filter(query).prefetch_related("user_phone").order_by("id")
        else:
            customer_list = User.objects.filter(id=self.request.user.id)
        return customer_list

    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            self.template_name = "admin/customer.html"
        queryset = self.get_queryset()
        self.context.update({"customer_list": queryset})
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        return redirect("index")
