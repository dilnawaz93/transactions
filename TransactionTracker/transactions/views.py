# # Standard Library Imports
#
#
# # Third-party imports
from rest_framework.views import APIView
from .serializers import TransactionSerializer, TransactionTypesSerializer
from django.http import JsonResponse
from rest_framework import status


# from rest_framework import status,permissions
# from django.http import JsonResponse
#
#
# Local source tree imports
from .models import Transaction,TransactionType
#
# logger = get_logger(__name__)
#
#


class TransactionsView(APIView):
    def get(self,request, transaction_id):
        transaction_obj = Transaction.objects.filter(transaction_id=int(transaction_id))
        serializer = TransactionSerializer(transaction_obj,many=True)
        return JsonResponse(serializer.data,safe=False)

    def put(self,request,transaction_id):
        data = request.data
        data['transaction_id']=int(transaction_id)
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



class TransactionTypesView(APIView):
    def get(self,request,type):
        transaction_type_obj= Transaction.objects.filter(type=type.lower())
        serializer=TransactionSerializer(transaction_type_obj,many=True)
        return JsonResponse(serializer.data, safe=False)
