from django.db import models
from django.utils import timezone
import datetime


class Productlar(models.Model):
    kod = models.IntegerField()
    adi = models.CharField(max_length=250)
    qiymeti =models.DecimalField(max_digits=10, decimal_places=2)
    miqdari = models.IntegerField()
    gram = models.IntegerField(null=False)
    publish = models.DateTimeField(default=timezone.now)
    status =models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.adi} | kod: {self.kod}"

    class Meta:
        verbose_name = 'Mehsullar cedveli'
        verbose_name_plural = 'Mehsullar'