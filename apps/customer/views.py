from django.shortcuts import render, redirect
from apps.customer import models
from apps.core.models import User
from django.views.generic import ListView, TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate


class IndexView(TemplateView):
    template_name = "index.html"
    context = {}

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        return redirect("index")


class LoginView(TemplateView):
    template_name = "customer/login.html"
    context = {}

    def get(self, *args, **kwargs):
        # self.context.update(kwargs)
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


class LogoutView(RedirectView):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect("index")


class RegisterView(TemplateView):
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
        return redirect("index")


class CustomerView(LoginRequiredMixin, TemplateView):
    template_name = "customer/customer.html"
    context = {}

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        user = User.objects.create_user(kwargs)
        print(user)
        return redirect()
