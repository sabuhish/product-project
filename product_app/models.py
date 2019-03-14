from django.db import models
from django.utils import timezone
import datetime
from PIL import Image
from django.utils.translation import ugettext_lazy as _

# label="malin adi"
# ,uppercase=True
class Productlar(models.Model):
    STATUS_CREATED = 1
    STATUS_SOLD_OUT = 2
    STATUS_REJECTED = 3


# is_staff = models.BooleanField( default=False,
# help_text=_('Designates whether the user can log into this admin '
# 'site.'))

    kod = models.IntegerField(help_text=_('Məhsulun kodunu qeyd edin. '))
    adi = models.CharField(max_length=250,help_text=_('Məhsulun adını qeyd edin. '))
    eyar = models.IntegerField(blank=False, null=True,help_text=_('Məhsulun əyarını qeyd edin. '))
    alis_qiymeti = models.DecimalField(max_digits=10, decimal_places=2,help_text=_('Məhsulu aldıgınız qiyməti qeyd edin. '))
    satis_qiymeti = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text=_('Məhsulu planlaşdırğınız satış qiymətini daxil edin ')) 
    miqdari = models.IntegerField()
    gram = models.DecimalField(null=False, max_digits=10, decimal_places=2,help_text=_('Qramı ilə bağlı məlumat daxil edin. ')) 
    mezenne = models.DecimalField(blank=False, null=True, max_digits=10, decimal_places=3, help_text=_('Bugünün məzənnəsinə uyğun yazın '))
    publish = models.DateTimeField(default=timezone.now)
    publish_1 = models.DateTimeField(default=timezone.now, null=True, blank=True, help_text=_('Tarixi qeyd edin zehmet olmasa. '))
    status = models.IntegerField(choices=(
        (STATUS_CREATED, 'Satisda'),
        (STATUS_SOLD_OUT, "Satildi"),
        (STATUS_REJECTED, "İmtina edildi")
    ), default=STATUS_CREATED)
    
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.adi} | kod: {self.kod}"

    class Meta:
        verbose_name = 'Mehsullar cedveli'
        verbose_name_plural = 'Mehsullar'
        ordering = ["-id"]


# from django.utils.six import with_metaclass


# class UpperCharField(with_metaclass(models.CharField)):
#     def __init__(self, *args, **kwargs):
#         self.is_uppercase = kwargs.pop('uppercase', False)
#         super(UpperCharField, self).__init__(*args, **kwargs)

#     def get_prep_value(self, value):
#         value = super(UpperCharField, self).get_prep_value(value)
#         if self.is_uppercase:
#             return value.upper()

#         return value
class Images(models.Model):
    sekil = models.ForeignKey('Productlar', on_delete=models.CASCADE)
    image =models.ImageField(blank=True, default='default.jpg', null=True,max_length=250, upload_to="pictures", height_field=None, width_field=None)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name = 'Şəkil'
        verbose_name_plural = 'Şəkillər'
        ordering = ["-id"]


    def __str__(self):
        return f"{self.sekil}"
