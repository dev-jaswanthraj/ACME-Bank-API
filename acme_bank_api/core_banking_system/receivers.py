from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from acme_bank_api.core_banking_system.models import Transaction, Account


@receiver(pre_save, sender=Transaction)
def debit(sender, instance, **kwargs):
    if Transaction.trn_type == 'D':
        instance = Account.objects.get(pk=Transaction.account.primary_key)
        instance.balance -= Transaction.trn_amount
        instance.save()


@receiver(post_save, sender=Transaction)
def credit(sender, instance, created, **kwargs):
    if Transaction.trn_type == 'C':
        act = Account.objects.get(pk=Transaction.account.primary_key)
        act.balance -= Transaction.trn_amount
        act.save()
