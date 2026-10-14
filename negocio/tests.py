from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from .models import arriendo_equipo, equipo


class ArriendoEquipoTests(TestCase):
	def setUp(self):
		self.usuario = User.objects.create_user(username="arrendatario")
		self.equipo = equipo.objects.create(
			nombre="Equipo de prueba",
			descripcion="Equipo para probar el cálculo",
			usuario_creador=self.usuario,
			valor_equipo=10000,
		)

	def test_calcula_valor_total_segun_dias_arrendados(self):
		fecha_inicio = timezone.now()
		arriendo = arriendo_equipo.objects.create(
			equipo=self.equipo,
			fecha_inicio=fecha_inicio,
			fecha_fin=fecha_inicio + timedelta(days=3),
			usuario_arrendatario=self.usuario,
		)

		self.assertEqual(arriendo.valor_arriendo, Decimal("30000"))
