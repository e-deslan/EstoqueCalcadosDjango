from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'^alterado/$', views.alterado, name = 'alterado'),
	url(r'^cadastrar_calcado/$', views.cadastrar_calcado, name = 'cadastrar_calcado'),
	url(r'^exibir_calcado/$', views.exibir_calcado, name = 'exibir_calcado'),
	url(r'^busca_alterar_calcado/$', views.busca_alterar_calcado, name = 'busca_alterar_calcado'),
	url(r'^(?P<pk>\d+)/alterar_calcado/$', views.alterar_calcado, name = 'alterar_calcado'),
	url(r'^busca_excluir_calcado/$', views.busca_excluir_calcado, name = 'busca_excluir_calcado'),
	url(r'^(?P<pk>\d+)/excluir_calcado/$', views.excluir_calcado, name = 'excluir_calcado'),
	url(r'^cadastrar_cliente/$', views.cadastrar_cliente, name = 'cadastrar_cliente'),
	url(r'^exibir_cliente/$', views.exibir_cliente, name = 'exibir_cliente'),
	url(r'^busca_alterar_cliente/$', views.busca_alterar_cliente, name = 'busca_alterar_cliente'),
	url(r'^(?P<pk>\d+)/alterar_cliente/$', views.alterar_cliente, name = 'alterar_cliente'),
	url(r'^busca_excluir_cliente/$', views.busca_excluir_cliente, name = 'busca_excluir_cliente'),
	url(r'^(?P<pk>\d+)/excluir_cliente/$', views.excluir_cliente, name = 'excluir_cliente'),
	url(r'^cadastrar_estante/$', views.cadastrar_estante, name = 'cadastrar_estante'),
	url(r'^exibir_estante/$', views.exibir_estante, name = 'exibir_estante'),
	url(r'^busca_alterar_estante/$', views.busca_alterar_estante, name = 'busca_alterar_estante'),
	url(r'^(?P<pk>\d+)/alterar_estante/$', views.alterar_estante, name = 'alterar_estante'),
	url(r'^busca_excluir_estante/$', views.busca_excluir_estante, name = 'busca_excluir_estante'),
	url(r'^(?P<pk>\d+)/excluir_estante/$', views.excluir_estante, name = 'excluir_estante'),
	url(r'^iniciar_carrinho/$', views.iniciar_carrinho, name = 'iniciar_carrinho'),
	url(r'^exibir_carrinho/$', views.exibir_carrinho, name = 'exibir_carrinho'),
	url(r'^busca_add_calcado/$', views.busca_add_calcado, name = 'busca_add_calcado'),
	url(r'^(?P<pk>\d+)/add_calcado/$', views.add_calcado, name = 'add_calcado'),
	url(r'^busca_rem_calcado/$', views.busca_rem_calcado, name = 'busca_rem_calcado'),
	url(r'^(?P<pk>\d+)/rem_calcado/$', views.rem_calcado, name = 'rem_calcado'),
	url(r'^efetuar_venda/$', views.efetuar_venda, name = 'efetuar_venda'),
]