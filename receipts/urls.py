from django.urls import path


from .views import (
    ReceiptListView,
    ReceiptCreateView,
    AccountListView,
    ExpenseCategoryListView
)

urlpatterns = [
    path("", ReceiptListView.as_view(), name="home"),
    path("create/", ReceiptCreateView.as_view(), name="receipt_create"),
    path("categories/", ExpenseCategoryListView.as_view(),
         name="expense_category_list"),
    path("accounts/", AccountListView.as_view(), name="account_list")
]
