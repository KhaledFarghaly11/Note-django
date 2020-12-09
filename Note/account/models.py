from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class AmountUser(models.Model):
    amount = models.IntegerField(blank=True,null=True)
    user = models.ForeignKey(User , on_delete = models.CASCADE)




class Debose(models.Model):
    amount = models.ForeignKey(AmountUser , on_delete=models.CASCADE)
    debose = models.IntegerField()
    


class Debit(models.Model):
    amount = models.ForeignKey(AmountUser , on_delete=models.CASCADE)
    debit = models.IntegerField()
   

