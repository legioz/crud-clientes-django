from ninja import NinjaAPI, Query
from apps.customer import views
from apps.customer.API.schemas import Filters, Message, UserSchema
from typing import List
from ninja.responses import codes_4xx
from django.db.models import Q

api = NinjaAPI(title="CRM Crud", docs_url="/")


@api.get("customers", response={200: List[UserSchema], codes_4xx: Message})
def customers(request, filters: Filters = Query(None)):
    try:
        query = Q()
        if filters.is_active is not None:
            query &= Q(is_active=filters.is_active)
        if filters.email is not None:
            query &= Q(email__icontains=filters.email)
        if filters.first_name is not None:
            query &= Q(first_name__icontains=filters.first_name)
        if filters.last_name is not None:
            query &= Q(last_name__icontains=filters.last_name)
        view = views.CustomerView()
        view.request = request
        queryset = view.get_queryset().filter(query)
        print(queryset)
        return queryset
    except Exception as e:
        return 400, {"message": f"error: {e}"}
