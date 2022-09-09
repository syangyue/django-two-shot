from django.contrib import admin

from .models import ExpenseCategory, Account, Receipt

admin.site.register(ExpenseCategory)
admin.site.register(Account)
admin.site.register(Receipt)
