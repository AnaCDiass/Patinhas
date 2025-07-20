import app.views
print(dir(app.views))

from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    # Parte pública
    path('animais/', AnimaisView.as_view(), name='animais'),
    path('campanhas/', CampanhasView.as_view(), name='campanhas'),
    path('denuncias/', DenunciaView.as_view(), name='denuncias'),
    path('doacao/', DoacaoView.as_view(), name='doacao'),
    path('adocao/', AdocaoView.as_view(), name='adocao'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
    path('enderecos/', EnderecosView.as_view(), name='enderecos'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
    path('ocupacoes/', OcupacaoView.as_view(), name='ocupacao'),
    path('saude-animal/', SaudeAnimalView.as_view(), name='saude_animal'),

    # Parte privada (se for usar depois)
    # path('painel/', DashboardView.as_view(), name='dashboard'),
    # path('animal/novo/', CadastroAnimalView.as_view(), name='cadastro_animal'),
    # path('campanha/nova/', CadastroCampanhaView.as_view(), name='cadastro_campanha'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


