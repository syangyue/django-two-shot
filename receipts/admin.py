from django.contrib import admin

from .models import ExpenseCategory, Account, Receipt


class ExpenseCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)


class AccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(Account, AccountAdmin)


class ReceiptAdmin(admin.ModelAdmin):
    pass


admin.site.register(Receipt, ReceiptAdmin)
