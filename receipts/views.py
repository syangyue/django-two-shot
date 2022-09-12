from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Receipt,  ExpenseCategory, Account
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/receipt_list.html"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    template_name = "receipts/receipt_create.html"
    fields = ["vendor", "total", "tax", "date", "category", "account"]

    def form_valid(self, form):
        form.instance.purchaser = self.request.user
        return super().form_valid(form)


class ExpenseCategoryListView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = "receipts/expence_list.html"

    def get_queryset(self):
        return ExpenseCategory.objects.filter(owner=self.request.user)


class ExpenseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    template_name = "receipts/expence_create.html"
    fields = ["name", "owner"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.category = self.request.user
        item.save()
        return redirect("receipts/expence_list")


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "receipts/account_list.html"


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "receipts/account_create.html"
    fields = ["name", "number", "owner"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("/receipts/accounts/")
