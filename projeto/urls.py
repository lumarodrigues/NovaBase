"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from projeto.portfolio.views import home, autocad, curso_rapido, designer, dev_frontend, dev_games, \
    editor_videos, profissionalizante, projetista, rotinas_adm, dsmax, obrigado, desenvolvimento_web, html5, \
    css3, design_mecanico, autocad_base, autocad_3dcivil, autocad_mecanica_base, autocad_projeto_civil, solidworks, \
    revit_base, sketchup, design_grafico, after_effects, corel_draw, express, illustrator, indesign, photoshop, \
    photoshop_fotografia, premiere_pro, construct, edicao_youtube, informatica, informatica_kids, informatica_adultos, \
    internet, inteligencia_artificial, logica_programacao, windows, marketing, marketing_iniciantes, marketing_pessoal, \
    pacote_office, word, word_avancado, power_point, excel, access, administracao, atendimento_cliente, \
    balconista_farmacia, montagem_curriculo, contabilidade, digitacao, empreendedorismo, emprego_20, gestao_qualidade, \
    lideranca_gestao, logistica, operador_caixa, oratoria, secretariado, tecnicas_redacao, telemarketing, vendas, \
    matematica_financeira, departamento_pessoal, operador_computador, pacotes, profissionais, autocad_total, excel_total

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('autocad', autocad, name='autocad'),

    path('obrigado', obrigado, name='obrigado'),
    path('desenvolvimento_web', desenvolvimento_web, name='desenvolvimento_web'),
    path('desenvolvimento_web/html5', html5, name='html5'),
    path('desenvolvimento_web/css3', css3, name='css3'),
    path('design_mecanico', design_mecanico, name='design_mecanico'),
    path('design_mecanico/autocad_base', autocad_base, name='autocad_base'),
    path('design_mecanico/autocad_3dcivil', autocad_3dcivil, name='autocad_3dcivil'),
    path('design_mecanico/autocad_mecanica_base', autocad_mecanica_base, name='autocad_mecanica_base'),
    path('design_mecanico/autocad_projeto_civil', autocad_projeto_civil, name='autocad_projeto_civil'),
    path('design_mecanico/solidworks', solidworks, name='solidworks'),
    path('design_mecanico/revit_base', revit_base, name='revit_base'),
    path('design_mecanico/sketchup', sketchup, name='sketchup'),
    path('design_grafico', design_grafico, name='design_grafico'),
    path('design_grafico/3dsmax', dsmax, name='3dsmax'),
    path('design_grafico/after_effects', after_effects, name='after_effects'),
    path('design_grafico/corel_draw', corel_draw, name='corel_draw'),
    path('design_grafico/express', express, name='express'),
    path('design_grafico/illustrator', illustrator, name='illustrator'),
    path('design_grafico/indesign', indesign, name='indesign'),
    path('design_grafico/photoshop', photoshop, name='photoshop'),
    path('design_grafico/photoshop_fotografia', photoshop_fotografia, name='photoshop_fotografia'),
    path('design_grafico/premiere_pro', premiere_pro, name='premiere_pro'),
    path('design_grafico/construct', construct, name='construct'),
    path('design_grafico/edicao_youtube', edicao_youtube, name='edicao_youtube'),
    path('informatica', informatica, name='informatica'),
    path('informatica/informatica_kids', informatica_kids, name='informatica_kids'),
    path('informatica/informatica_adultos', informatica_adultos, name='informatica_adultos'),
    path('informatica/internet', internet, name='internet'),
    path('informatica/inteligencia_artificial', inteligencia_artificial, name='inteligencia_artificial'),
    path('informatica/logica_programacao', logica_programacao, name='logica_programacao'),
    path('informatica/windows', windows, name='windows'),
    path('marketing', marketing, name='marketing'),
    path('marketing/marketing_iniciantes', marketing_iniciantes, name='marketing_iniciantes'),
    path('marketing/marketing_pessoal', marketing_pessoal, name='marketing_pessoal'),
    path('pacote_office', pacote_office, name='pacote_office'),
    path('pacote_office/word', word, name='word'),
    path('pacote_office/word_avancado', word_avancado, name='word_avancado'),
    path('pacote_office/power_point', power_point, name='power_point'),
    path('pacote_office/excel', excel, name='excel'),
    path('pacote_office/access', access, name='access'),
    path('profissionais', profissionais, name='profissionais'),
    path('profissionais/administracao', administracao, name='administracao'),
    path('profissionais/atendimento_cliente', atendimento_cliente, name='atendimento_cliente'),
    path('profissionais/balconista_farmacia', balconista_farmacia, name='balconista_farmacia'),
    path('profissionais/montagem_curriculo', montagem_curriculo, name='montagem_curriculo'),
    path('profissionais/contabilidade', contabilidade, name='contabilidade'),
    path('profissionais/departamento_pessoal', departamento_pessoal, name='departamento_pessoal'),
    path('profissionais/digitacao', digitacao, name='digitacao'),
    path('profissionais/empreendedorismo', empreendedorismo, name='empreendedorismo'),
    path('profissionais/emprego_20', emprego_20, name='emprego_20'),
    path('profissionais/gestao_qualidade', gestao_qualidade, name='gestao_qualidade'),
    path('profissionais/lideranca_gestao', lideranca_gestao, name='lideranca_gestao'),
    path('profissionais/logistica', logistica, name='logistica'),
    path('profissionais/operador_caixa', operador_caixa, name='operador_caixa'),
    path('profissionais/oratoria', oratoria, name='oratoria'),
    path('profissionais/secretariado', secretariado, name='secretariado'),
    path('profissionais/tecnicas_redacao', tecnicas_redacao, name='tecnicas_redacao'),
    path('profissionais/telemarketing', telemarketing, name='telemarketing'),
    path('profissionais/vendas', vendas, name='vendas'),
    path('profissionais/matematica_financeira', matematica_financeira, name='matematica_financeira'),
    path('pacotes', pacotes, name='pacotes'),
    path('pacotes/operador_computador', operador_computador, name='operador_computador'),
    path('pacotes/profissionalizante', profissionalizante, name='profissionalizante'),
    path('pacotes/curso_rapido', curso_rapido, name='curso_rapido'),
    path('pacotes/designer', designer, name='designer'),
    path('pacotes/editor_videos', editor_videos, name='editor_videos'),
    path('pacotes/autocad_total', autocad_total, name='autocad_total'),
    path('pacotes/dev_frontend', dev_frontend, name='dev_frontend'),
    path('pacotes/dev_games', dev_games, name='dev_games'),
    path('pacotes/editor_videos', editor_videos, name='editor_videos'),
    path('pacotes/projetista', projetista, name='projetista'),
    path('pacotes/rotinas_adm', rotinas_adm, name='rotinas_adm'),
    path('pacotes/excel_total', excel_total, name='excel_total'),


]
