from django.http import HttpResponse
from .forms import CalcadoForm, BuscaForm, ClienteForm, VendaForm, EstanteForm, CarrinhoForm
from django.shortcuts import redirect, get_object_or_404, render
from .models import Calcado, Cliente, Venda, Estante

def home(request):
	return render(request, 'calcados/home.html', {})

def alterado(request):
	return render(request, 'calcados/alterado.html', {})

#----------------Calcados---------------------------

def cadastrar_calcado(request):
	if request.method == 'POST':
		form = CalcadoForm(request.POST)
		if form.is_valid():
			calcado = form.save()
			calcado.save()
			return redirect('/calcados/alterado/')
		else:
			return render(request, 'calcados/cadastrar.html', {'form': form})
	else:
		form = CalcadoForm()
		return render(request, 'calcados/cadastrar.html', {'form': form})

def exibir_calcado(request):
	if request.method == 'POST':
		form = BuscaForm(request.POST)
		if form.is_valid():
			pk = form.cleaned_data['chave']
			calcado = get_object_or_404(Calcado, pk = pk)
			form = CalcadoForm(instance = calcado)
			return render(request, 'calcados/exibir.html', {'form': form})
	else:
		form = BuscaForm()
		return render(request, 'calcados/busca.html', {'form': form})

def busca_alterar_calcado(request):
	if request.method == 'POST':
		form = BuscaForm(request.POST)
		if form.is_valid():
			pk = form.cleaned_data['chave']
			return redirect('alterar_calcado', pk = pk)
	else:
		form = BuscaForm()
		return render(request, 'calcados/busca.html', {'form': form})

def alterar_calcado(request, pk):
	calcado = get_object_or_404(Calcado, pk = pk)
	if request.method == 'POST':
		form = CalcadoForm(request.POST, instance = calcado)
		if form.is_valid():
			calcado = form.save()
			calcado.save()
			return redirect('/calcados/alterado/')
	else:
		form = CalcadoForm(instance = calcado)
		return render(request, 'calcados/cadastrar.html', {'form': form})

def busca_excluir_calcado(request):
	if request.method == 'POST':
		form = BuscaForm(request.POST)
		if form.is_valid():
			pk = form.cleaned_data['chave']
			return redirect('excluir_calcado', pk = pk)
	else:
		form = BuscaForm()
		return render(request, 'calcados/busca.html', {'form': form})

def excluir_calcado(request, pk):
	calcado = get_object_or_404(Calcado, pk = pk)
	if request.method == 'POST':
		form = CalcadoForm(request.POST, instance = calcado)
		if form.is_valid():
			calcado = form.save()
			calcado.delete()
			return redirect('/calcados/alterado/')
	else:
		form = CalcadoForm(instance = calcado)
		return render(request, 'calcados/excluir.html', {'form': form})

#------------------------Clientes---------------------------------

def cadastrar_cliente(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			cliente = form.save()
			cliente.save()
			return redirect('/calcados/alterado/')
		else:
			return render(request, 'calcados/cadastrar.html', {'form': form})
	else:
		form = ClienteForm()
		return render(request, 'calcados/cadastrar.html', {'form': form})

def exibir_cliente(request):
	if request.method == 'POST':
		form = BuscaForm(request.POST)
		if form.is_valid():
			pk = form.cleaned_data['chave']
			cliente = get_object_or_404(Cliente, pk = pk)
			form = ClienteForm(instance = cliente)
			return render(request, 'calcados/exibir.html', {'form': form})
	else:
		form = BuscaForm()
		return render(request, 'calcados/busca.html', {'form': form})

def busca_alterar_cliente(request):
	if request.method == 'POST':
		form = BuscaForm(request.POST)
		if form.is_valid():
			pk = form.cleaned_data['chave']
			return redirect('alterar_cliente', pk = pk)
	else:
		form = BuscaForm()
		return render(request, 'calcados/busca.html', {'form': form})

def alterar_cliente(request, pk):
	cliente = get_object_or_404(Cliente, pk = pk)
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance = cliente)
		if form.is_valid():
			cliente = form.save()
			cliente.save()
			return redirect('/calcados/alterado/')
	else:
		form = ClienteForm(instance = cliente)
		return render(request, 'calcados/cadastrar.html', {'form': form})

def busca_excluir_cliente(request):
	if request.method == 'POST':
		form = BuscaForm(request.POST)
		if form.is_valid():
			pk = form.cleaned_data['chave']
			return redirect('excluir_cliente', pk = pk)
	else:
		form = BuscaForm()
		return render(request, 'calcados/busca.html', {'form': form})

def excluir_cliente(request, pk):
	cliente = get_object_or_404(Cliente, pk = pk)
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance = cliente)
		if form.is_valid():
			cliente = form.save()
			cliente.delete()
			return redirect('/calcados/alterado/')
	else:
		form = ClienteForm(instance = cliente)
		return render(request, 'calcados/excluir.html', {'form': form})

#---------------------Estantes-----------------------------------------

def cadastrar_estante(request):
	if request.method == 'POST':
		form = EstanteForm(request.POST)
		if form.is_valid():
			estante = form.save()
			estante.save()
			return redirect('/calcados/alterado/')
		else:
        # caso o formulario tenha erro:
			return render(request, 'calcados/cadastrar.html', {'form': form})
	else:
		form = EstanteForm()
		return render(request, 'calcados/cadastrar.html', {'form': form})

def exibir_estante(request):
	if request.method == 'POST':
		form = BuscaForm(request.POST)
		if form.is_valid():
			pk = form.cleaned_data['chave']
			estante = get_object_or_404(Estante, pk = pk)
			return render(request, 'calcados/exibir_estante.html', {'estante': estante})
	else:
		form = BuscaForm()
		return render(request, 'calcados/busca.html', {'form': form})

def busca_alterar_estante(request):
	if request.method == 'POST':
		form = BuscaForm(request.POST)
		if form.is_valid():
			pk = form.cleaned_data['chave']
			return redirect('alterar_estante', pk = pk)
	else:
		form = BuscaForm()
		return render(request, 'calcados/busca.html', {'form': form})

def alterar_estante(request, pk):
	estante = get_object_or_404(Estante, pk = pk)
	if request.method == 'POST':
		form = EstanteForm(request.POST, instance = estante)
		if form.is_valid():
			estante = form.save()
			estante.save()
			return redirect('/calcados/alterado/')
	else:
		form = EstanteForm(instance = estante)
		return render(request, 'calcados/cadastrar.html', {'form': form})

def busca_excluir_estante(request):
	if request.method == 'POST':
		form = BuscaForm(request.POST)
		if form.is_valid():
			pk = form.cleaned_data['chave']
			return redirect('excluir_estante', pk = pk)
	else:
		form = BuscaForm()
		return render(request, 'calcados/busca.html', {'form': form})

def excluir_estante(request, pk):
	estante = get_object_or_404(Estante, pk = pk)
	if request.method == 'POST':
		form = EstanteForm(request.POST, instance = estante)
		if form.is_valid():
			estante = form.save()
			estante.delete()
			return redirect('/calcados/alterado/')
	else:
		form = EstanteForm(instance = estante)
		return render(request, 'calcados/excluir.html', {'form': form})

#-----------------------Carrinho-----------------------------------------

def busca_add_calcado(request):
	if request.method == 'POST':
		form = BuscaForm(request.POST)
		if form.is_valid():
			pk = form.cleaned_data['chave']
			return redirect('add_calcado', pk = pk)
	else:
		form = BuscaForm()
		return render(request, 'calcados/busca.html', {'form': form})

def add_calcado(request, pk):
	calcado = get_object_or_404(Calcado, pk = pk)
	if request.method == 'POST':
		form = CalcadoForm(request.POST, instance = calcado)
		if form.is_valid():
			calcado = form.save()
			calcado.status = 'c'
			venda = Venda.objects.latest('data')
			venda.calcado_set.add(calcado)
			venda.atualiza_total()
			venda.save()
			return redirect('/calcados/exibir_carrinho/')
	else:
		form = CalcadoForm(instance = calcado)
		return render(request, 'calcados/adicionar.html', {'form': form})

def busca_rem_calcado(request):
	if request.method == 'POST':
		form = BuscaForm(request.POST)
		if form.is_valid():
			pk = form.cleaned_data['chave']
			return redirect('rem_calcado', pk = pk)
	else:
		form = BuscaForm()
		return render(request, 'calcados/busca.html', {'form': form})

def rem_calcado(request, pk):
	calcado = get_object_or_404(Calcado, pk = pk)
	if request.method == 'POST':
		form = CalcadoForm(request.POST, instance = calcado)
		if form.is_valid():
			calcado = form.save()
			calcado.status = 'e'
			calcado.save()
			venda = Venda.objects.latest('data')
			venda.calcado_set.remove(calcado)
			venda.atualiza_total()
			venda.save()
			return redirect('/calcados/exibir_carrinho/')
	else:
		form = CalcadoForm(instance = calcado)
		return render(request, 'calcados/remover.html', {'form': form})

def exibir_carrinho(request):
	venda = Venda.objects.latest('data')
	return render(request, 'calcados/exibir_carrinho.html', {'venda': venda})

def iniciar_carrinho(request):
	if request.method == 'POST':
		form = CarrinhoForm(request.POST)
		if form.is_valid():
			venda = form.save()
			venda.save()
			return redirect('/calcados/exibir_carrinho/', {'venda': venda})
		else:
			return render(request, 'calcados/cadastrar.html', {'form': form})
	else:
		form = CarrinhoForm()
		return render(request, 'calcados/cadastrar.html', {'form': form})

def efetuar_venda(request):
	venda = Venda.objects.latest('data')
	if request.method == 'POST':
		form = VendaForm(request.POST, instance = venda)
		if form.is_valid():
			venda = form.save()
			venda.altera_status_itens()
			venda.status = 'f'
			venda.save()
			return redirect('/calcados/exibir_carrinho/', {'venda': venda})
		else:
			return render(request, 'calcados/efetuar_venda.html', {'form': form, 'venda': venda})
	else:
		form = VendaForm(instance = venda)
		return render(request, 'calcados/efetuar_venda.html', {'form': form, 'venda': venda})

