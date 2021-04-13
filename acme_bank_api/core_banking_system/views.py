from acme_bank_api.core_banking_system.serializers import AccountSerializer, TransactionSerializer, \
    AccountTransactionSerializer
from acme_bank_api.core_banking_system.models import Transaction, Account
from rest_framework import permissions
from acme_bank_api.core_banking_system.permissions import IsAdminOrReadOnly
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status


class AccountCreate(APIView):
    permission_classes = (IsAdminOrReadOnly, permissions.IsAuthenticated)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountList(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAdminOrReadOnly, permissions.IsAuthenticated)


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountTransactionSerializer
    permission_classes = (IsAdminOrReadOnly, permissions.IsAuthenticated)
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        trans = Transaction.objects.filter(account=instance.id).all()
        c_amount = 0
        d_amount = 0
        for a in trans:
            if a.trn_type == 'D':
                d_amount = d_amount + a.trn_amount
            else:
                c_amount = c_amount + a.trn_amount
        closing_balance = instance.balance+c_amount-d_amount
        instance.closing_balance = closing_balance           
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class TransactionList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAdminOrReadOnly, permissions.IsAuthenticated)


class TransactionCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'accounts': reverse('account-list', request=request, format=format),
        'transactions': reverse('trans-list', request=request, format=format),
    })
