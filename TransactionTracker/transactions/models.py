from django.db import models

class TransactionType(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "transaction_type"


class Transaction(models.Model):
    transaction_id = models.BigIntegerField(unique=True,null=False)
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    type = models.CharField(max_length=500,null=False)
    parent_id = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        db_table = "transaction"



