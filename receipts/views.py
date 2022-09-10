from django.views.generic.list import ListView
from .models import Receipt


class ReceiptListView(ListView):
    model = Receipt
    template_name = "receipt/list.html"
