from django.urls import path

from .views import (
    ReceiptListView
)

urlpatterns = [
    path("", ReceiptListView.as_view(), name="receipt_list")
]
