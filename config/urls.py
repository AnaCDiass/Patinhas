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
    path('denuncia/', DenunciaView.as_view(), name='denuncia'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('doacao/', DoacaoView.as_view(), name='doacao'),

    # Parte privada (se for usar depois)
    # path('painel/', DashboardView.as_view(), name='dashboard'),
    # path('animal/novo/', CadastroAnimalView.as_view(), name='cadastro_animal'),
    # path('campanha/nova/', CadastroCampanhaView.as_view(), name='cadastro_campanha'),
]
