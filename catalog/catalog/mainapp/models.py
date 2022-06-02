from django.db import models


class Provider(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=128,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "поставщик"
        verbose_name_plural = "поставщики"


class Measure(models.Model):
    name = models.CharField(
        verbose_name='единица измерения',
        max_length=128,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "единица измерения"
        verbose_name_plural = "единицы измерения"


class Section(models.Model):
    name = models.CharField(
        verbose_name='раздел',
        max_length=128,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "pаздел"
        verbose_name_plural = "pазделы"


class Catalog(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=128,
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    add_time = models.DateField(
        verbose_name='дата поступления',
    )
    measure = models.ForeignKey(
        Measure,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='единица измерения',
    )
    provider = models.ForeignKey(
        Provider,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='поставщик',
    )
    sections = models.ManyToManyField(
        Section,
        verbose_name='разделы',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

