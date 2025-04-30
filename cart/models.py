from django.db import models

from db_admin.models import Prises, Users

# Create your models here.
class CartItem(models.Model):
    prise = models.ForeignKey(Prises, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'