from django.db import models
from profiles.models import Application
from django.contrib.auth.models import User


class ProductType(models.Model):
    created_dt = models.DateTimeField('Created at')
    created_by = models.ForeignKey(User, related_name="product_created_by")
    last_changed_dt = models.DateTimeField('Last Changed At')
    last_changed_by = models.ForeignKey(User, related_name="last_changed_by")
    name = models.CharField(max_length=90, null=False, blank=False)
    base_renewal_period_days=models.IntegerField(null=False, default=30)


class FeeType(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)
    input_vars_dict = models.TextField()
    formula = models.TextField()

    def apply(self, balance, **kwargs):
        pass





class Product(models.Model):
    created_dt = models.DateTimeField('Created at')
    created_by = models.ForeignKey(User, related_name="created_by")
    last_changed_dt = models.DateTimeField('Last Changed At')
    last_changed_by = models.ForeignKey(User, related_name="changed_by")
    minimum_term = models.IntegerField('Fixed term')
    current_apr = models.DecimalField(max_digits=10, decimal_places=2)
    #overrides the renewal period on ProductType if not null
    renewal_period_days=models.IntegerField(null=True, default=30)



class ProductAPRLog(models.Model):
    #TODO: Should APR changes apply imediatelly or on the next business day?
    product = models.ForeignKey(Product)
