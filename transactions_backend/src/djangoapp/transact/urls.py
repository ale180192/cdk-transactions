from django.urls import path

from . import views

urlpatterns = [
    path('summary', views.summary),
    path('companies/<str:company_id>', views.company_detail)
]