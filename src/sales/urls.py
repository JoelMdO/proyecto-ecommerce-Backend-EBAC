from django.urls import path
from sales import views

urlpatterns = [
    path("sales", views.SalesView.as_view(), name="sales"),
    path("sales/chart/data", views.SalesAjaxDashboardView.as_view(), name="sales_chart")
]