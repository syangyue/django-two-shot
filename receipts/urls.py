from django.urls import path


from receipts.views import (
    ReceiptListView,
    ReceiptCreateView,
    ExpenseCategoryListView,
    ExpenseCategoryCreateView,
    AccountListView,
    AccountCreateView
)

urlpatterns = [
    path("", ReceiptListView.as_view(), name="home"),
    path("create/", ReceiptCreateView.as_view(), name="create_receipt"),
    path("categories/", ExpenseCategoryListView.as_view(),
         name="expence_list"),
    path("accounts/", AccountListView.as_view(), name="account_list"),
    path("categories/create/", ExpenseCategoryCreateView.as_view(),
         name="create_category"),
    path("accounts/create/", AccountCreateView.as_view(),
         name="create_account"),

]
