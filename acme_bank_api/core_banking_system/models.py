from django.db import models
from django.core.validators import RegexValidator


# from django.core.signals import request_finished


class Account(models.Model):
    ACCT_TYPE = (
        ('S', 'Savings'),
        ('C', 'Checking'),
    )
    HOLDING_PATTERN = (
        ('S', 'Single'),
        ('J', 'Joint'),
    )
    acct_num = models.IntegerField()
    acct_type = models.CharField(max_length=1, choices=ACCT_TYPE)
    hold_pattern = models.CharField(max_length=1, choices=HOLDING_PATTERN)
    currency = models.CharField(max_length=10)
    balance = models.FloatField()
    min_balance = models.FloatField()
    mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                  message="Phone number must be entered in the format: '+999999999'."
                                          "Up to 15 digits allowed.")
    mobile_number = models.CharField(validators=[mobile_regex], max_length=17, blank=False)
    date_of_birth = models.DateField()
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.acct_num)


class Transaction(models.Model):
    CREDIT = 'C'
    DEBIT = 'D'
    TRN_TYPE = (
        (CREDIT, 'Credit'),
        (DEBIT, 'Debit'),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    trn_date = models.DateField()
    trn_narration = models.CharField(max_length=100)
    trn_ref_no = models.CharField(max_length=20, null=True)
    trn_amount = models.FloatField()
    trn_type = models.CharField(max_length=1, choices=TRN_TYPE)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(
            self.trn_date, self.trn_narration, self.trn_ref_no, self.trn_amount, self.trn_type)

    class Meta:
        ordering = ('id',)
