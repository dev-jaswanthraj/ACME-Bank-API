from rest_framework import serializers
from acme_bank_api.core_banking_system.models import Transaction, Account


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('account', 'trn_date', 'trn_narration', 'trn_ref_no', 'trn_amount', 'trn_type')

    def create(self, validated_data):
        obj = Transaction.objects.create(**validated_data)
        return obj


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'acct_num', 'acct_type', 'hold_pattern', 'currency',
                  'balance', 'min_balance', 'mobile_number', 'date_of_birth', 'create_date')

    def create(self, validated_data):
        obj = Account.objects.create(**validated_data)
        return obj


class AccountTransactionSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(many=True, read_only=True)
    closing_balance = serializers.FloatField()

    class Meta:
        model = Account
        fields = ('url', 'acct_num', 'acct_type', 'hold_pattern', 'currency', 'balance',
                  'min_balance', 'create_date', 'transaction', 'closing_balance')
