from typing import Any
from django.http import HttpRequest, JsonResponse
from order_manager.models import OrderManagerModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View
#from django.shortcuts import render

class SalesView(LoginRequiredMixin, TemplateView):
    template_name = "sales/chart.html"

    def dispatch(self, *args: Any, **kargs: Any):
        user = self.request.user
        if not user.is_staff: # type: ignore #type :ignore
            return HttpResponse("No permitido", status=401)
        return super(SalesView, self).dispatch(*args, **kargs)
    
    def get_context_data(self, *args: Any, **kargs: Any):
       context = super(SalesView, self).get_context_data(*args, **kargs)
       qs = OrderManagerModel.objects.all()
       context["paid_orders"] = qs
       return context
    
class SalesAjaxDashboardView(View):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Any:
        data = {}
        qs = OrderManagerModel.objects.all()
        total_sales = sum(order.total for order in qs) # type: ignore
        print(total_sales)
        data["data"] = [float(total_sales)]  # Chart.js expects array
        data["labels"] = ["Total Sales"]
        return JsonResponse(data)