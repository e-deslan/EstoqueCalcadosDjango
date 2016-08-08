from django import forms
from .models import Calcado, Cliente, Venda, Estante
from localflavor.br.forms import BRCPFField

class CalcadoForm(forms.ModelForm):
	class Meta:
		model = Calcado
		fields = ('marca', 'modelo', 'tamanho', 'cor', 'preco', 'status', 'estante', 'prateleira')

class ClienteForm(forms.ModelForm):

	cpf = BRCPFField()

	class Meta:
		model = Cliente
		fields = ('nome', 'cpf', 'celular', 'tel_fixo', 'email', 'end')

class CarrinhoForm(forms.ModelForm):
	class Meta:
		model = Venda
		fields = ('cliente', 'vendedor')

class VendaForm(forms.ModelForm):
	class Meta:
		model = Venda
		fields = ('cliente', 'vendedor', 'forma_pagamento', 'total')

	def clean(self):
	    campos = self.cleaned_data
	    if campos['total'] < 50 and campos['forma_pagamento'] != 'v':
	        self._errors["forma_pagamento"] = ["Este valor nao permite dividir no cartao!"]
	        del campos['forma_pagamento']
	    return campos

class BuscaForm(forms.Form):
	chave = forms.IntegerField(label = 'Chave')

class EstanteForm(forms.ModelForm):
	class Meta:
		model = Estante
		fields = ('tipo', 'num_prateleiras')