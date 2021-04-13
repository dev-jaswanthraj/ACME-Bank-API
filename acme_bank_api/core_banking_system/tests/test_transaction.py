from django.urls import reverse
from acme_bank_api.core_banking_system.models import Account, Transaction
from rest_framework import status
from rest_framework.test import APITestCase


class TransactionTest(APITestCase):
