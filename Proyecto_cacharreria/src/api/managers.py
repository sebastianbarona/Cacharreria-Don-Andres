from time import strptime

from django.db import models


class ProveedorManager(models.Manager):

    def get_proveedor_by_created(self, my_date):
        date = strptime(my_date, '%Y-%m-%d')
        queryset = self.get_queryset()
        return queryset.filter(createdAt__year=date.tm_year,
                               createdAt__month=date.tm_mon,
                               createdAt__day=date.tm_mday)