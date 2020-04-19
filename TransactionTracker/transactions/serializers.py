from rest_framework import serializers
from .models import Transaction,TransactionType


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class TransactionSerializer(serializers.ModelSerializer):
    parent_id=RecursiveField(many=True)
    class Meta:
        model = Transaction
        fields = ['transaction_id','amount','type','parent_id']


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Transaction.objects.create(**validated_data)

class TransactionTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ['id','name']