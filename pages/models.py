from django.db import models


# Create your models here.
class CalcMeasure(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CalcHscode(models.Model):

    class Meta:
        ordering = ('id',)

    measureCode = models.ForeignKey(CalcMeasure, on_delete=models.CASCADE)
    code = models.CharField("Код ТНВЭД:", max_length=10)
    name = models.CharField("Наименование товарной позиции", max_length=255)
    rate = models.CharField(
        "Ставка ввозной таможенной пошлины", max_length=255)


class ImageSite(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    cover = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
  