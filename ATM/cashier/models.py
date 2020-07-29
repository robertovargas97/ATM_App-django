from django.db import models

# Create your models here.


class Transaction(models.Model):
    amount = models.IntegerField()
    transaction_date = models.DateTimeField('transaction date')
    result = models.CharField(max_length = 100)

    def __str__(self):
        return "id : %d  , result : %s " % (self.id, self.result)
