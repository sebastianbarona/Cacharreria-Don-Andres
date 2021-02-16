import datetime
import json
from time import strftime

import pytest
from django.urls import reverse
from django_mock_queries.query import MockSet
from rest_framework.exceptions import ValidationError

from .models import Proveedor
from .serializers import ProveedorSerializer
from .views import  ProveedoresView



class TestProveedorModels:

    def test_get_proveedor_by_created(self, mocker):
        expected_results = [
            Proveedor(id_proveedor='1',
                nombre_proveedor = 'Jhon',
                cantidad_articulos = 1000,
                precio_producto = 2000)
                      
        ]

        date = strftime('%Y-%m-%d')
        # django-mock-queries nos permite crear Mock QuerySets
        # para omitir el acceso a BD
        qs = MockSet(expected_results[0])

        # Patch el metodo qet_queryset para modificar su comportamiento
        # y que nos retorne nuestro queryset  y asi omitir el acceso
        # a BD
        mocker.patch.object(Proveedor.objects, 'get_queryset', return_value=qs)

        result = list(Proveedor.objects.get_proveedor_by_created(date))

        assert result == expected_results
        assert str(result[0]) == expected_results[0].nombre_proveedor


class TestProveedorSerializer:

    def test_expected_serialized_json(self):
        expected_results = {
            'id_proveedor':'123458',
            'nombre_proveedor': 'Sebastian',
            'cantidad_articulos': 1000,
            'precio_producto': 2000,
               
        }

        proveedor = Proveedor(**expected_results)

        results = ProveedorSerializer(proveedor).data

        assert results == expected_results

    def test_raise_error_when_missing_required_field(self):
        incomplete_data = {
            'id_proveedor': '12345',
            'nombre_proveedor': 'Manuel',
            'cantidad_articulos': 2000,
            'precio_producto': 1000,
        }

        serializer = ProveedorSerializer(data=incomplete_data)

        # Este ContextManager nos permite verificar que
        # se ejecute correctamente una Excepcion
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)



