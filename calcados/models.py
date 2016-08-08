from django.db import models
from django.utils import timezone

class Cliente(models.Model):
	nome = models.CharField(max_length = 60)
	cpf = models.CharField(primary_key = True, max_length = 14)
	celular = models.CharField(max_length = 11)
	tel_fixo = models.CharField(max_length = 11)
	email = models.EmailField()
	end = models.CharField(max_length = 100)
	data_cadastro = models.DateField(auto_now_add = True)

	def __str__(self):
		return self.nome

class Funcionario(models.Model):
	nome = models.CharField(max_length = 60)
	cpf = models.CharField(unique = True, max_length = 14)
	num_func = models.IntegerField(primary_key = True)
	celular = models.CharField(max_length = 11)
	tel_fixo = models.CharField(max_length = 11)
	email = models.EmailField()
	end = models.CharField(max_length = 100)
	comissao_venda = models.DecimalField(max_digits = 4, decimal_places = 2)

	def __str__(self):
		return self.nome

class Estante(models.Model):
	tipoChoices = (
		('v','vitrine'),
		('d','deposito'),
	)
	tipo = models.CharField(max_length = 1, choices = tipoChoices)
	num_prateleiras = models.IntegerField()

	def __str__(self):
		return "Estante " + str(self.id)

class Calcado(models.Model):
	statusChoices = (
		('v', 'vendido'),
		('e', 'na estante'),
		('c', 'no carrinho'),
	)
	marca = models.CharField(max_length = 20)
	modelo = models.CharField(max_length = 20)
	tamanho = models.IntegerField()
	cor = models.CharField(max_length = 20)
	preco = models.DecimalField(max_digits = 6, decimal_places = 2)
	estante = models.ForeignKey(Estante, null = True, blank = True, on_delete = models.SET_NULL)
	prateleira = models.IntegerField()
	status = models.CharField(max_length = 1, choices = statusChoices, default = 'e')
	carrinho = models.ForeignKey('Venda', null = True, blank = True, editable = False, on_delete = models.SET_NULL)

	def __str__(self):
		return " (" + str(self.id) + ") " + self.marca + " " + self.modelo + " [tam " + str(self.tamanho) + "]"

class Venda(models.Model):
	formasP = (
		('v', 'a vista'),
		('2x', '2x no cartao'),
		('4x', '4x no cartao'),
		('6x', '6x no cartao'),
		('8x', '8x no cartao'),
		('10x', '10x no cartao'),
	)
	statusV = (
		('a','em andamento'),
		('f','finalizado'),
	)
	cliente = models.ForeignKey(Cliente, on_delete = models.PROTECT)
	vendedor = models.ForeignKey(Funcionario, on_delete = models.PROTECT)
	status = models.CharField(max_length = 1, choices = statusV, default = 'a')
	total = models.DecimalField(max_digits = 6, decimal_places = 2, default = 0)
	forma_pagamento = models.CharField(max_length = 3, choices = formasP, blank = True, null = True)
	data = models.DateTimeField(auto_now_add = True)

	def atualiza_total(self):
		total = 0
		for item in self.calcado_set.all():
			total += item.preco
		self.total = total

	def altera_status_itens(self):
		for item in self.calcado_set.all():
			item.status = 'v'
			item.estante = None
			item.prateleira = 0
			item.save()

	def __str__(self):
		return "venda de " + self.cliente.nome + " em " + str(self.data)
