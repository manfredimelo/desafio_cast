"""desafio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.db import router
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from base.views.index import index
from base.views.login import login_restrito
from base.views.logout import logout
from rest_framework.authtoken.views import obtain_auth_token
from base.views.manter_produto import ProdutoCreateView, ProdutoListView, ProdutoUpdateView, classificacao_produto
from processamento.api.viewsets import ClassificacaoViewSet
from processamento.views.manter_regra import RegraListView, RegraCreateView, RegraUpdateView
from rest_framework import routers

_read_only = {'get': 'list'}


router = routers.DefaultRouter()
# router.register(r'classificacoes', ClassificacaoViewSet, base_name='Classificacao')

urlpatterns = [

    path('rotas/classificacoes/', ClassificacaoViewSet.as_view(_read_only), name='classificacao-list'),
    # path('rotas/', include(router.urls)),
    path('', login_restrito, name='login'),
    url(r'index', index, name='index'),
    url(r'^sair/$', logout, name='logout'),
    url(r'^produtos/$', login_required(ProdutoListView.as_view()), name='listar_produtos'),
    url(r'^produtos/cadastrar/$', ProdutoCreateView.as_view(), name="cadastrar_produto"),
    url(r'^produtos/editar/(?P<id_produto>\d+)/$', ProdutoUpdateView.as_view(), name="editar_produto"),

    url(r'^regras/$', login_required(RegraListView.as_view()), name="listar_regras"),
    url(r'^regras/cadastrar/$', RegraCreateView.as_view(), name="cadastrar_regra"),
    url(r'^regras/editar/(?P<id_regra>\d+)/$', RegraUpdateView.as_view(), name="editar_regra"),
    url(r'produtos/classificacao_produto/(?P<id_produto>\d+)/$', classificacao_produto, name='classificacao_produto'),

    path('api-token-auth/', obtain_auth_token),
    # path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
