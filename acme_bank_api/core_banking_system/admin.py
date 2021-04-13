from django.contrib import admin

# Register your models here.
from acme_bank_api.core_banking_system.models import Account, Transaction

admin.site.register(Account)
admin.site.register(Transaction)
