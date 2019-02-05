# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    name = models.CharField(
        verbose_name=_('category name'),
        help_text=_('provide a category name'),
        max_length=128
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Product(models.Model):
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    name = models.CharField(
        verbose_name=_('p;roduct name'),
        help_text=_('provide a product name'),
        max_length=128
    )
    price = models.FloatField()

    category = models.ForeignKey(
        to='core.Category',
        on_delete=models.PROTECT,
        related_name='products'
    )

    is_active = models.BooleanField(
        verbose_name=_('is product active?'),
        default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})
