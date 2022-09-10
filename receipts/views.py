from django.views.generic.list import ListView
from .models import Receipt
from django.contrib.auth.mixins import LoginRequiredMixin


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipt/list.html"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)
