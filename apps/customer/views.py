from django.shortcuts import render, redirect
from apps.customer import models
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomerView(LoginRequiredMixin, TemplateView):
    template_name = ""
    context = {

    }

    def get(self, *args, **kwargs):
        render(self.request, self.template_name, self.context)
    
    def post(self, *args, **kwargs):
        return redirect()