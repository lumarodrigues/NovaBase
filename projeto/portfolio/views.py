from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from projeto.forms import ContactForm
from django.http import HttpResponse

from projeto.settings import EMAIL_USER


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        try:
            send_mail('Mensagem de ' + name, 'Nome: ' + name + '\nEmail: ' + email + '\nTelefone: ' + phone + '\n\nMensagem: ' + message,
                      [EMAIL_USER], [EMAIL_USER], fail_silently=False,)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect(obrigado)

    return render(request, 'portfolio/base.html')


def operador_computador(request):
    return render(request, 'portfolio/operador_computador.html')


def curso_rapido(request):
    return render(request, 'portfolio/curso_rapido.html')


def designer(request):
    return render(request, 'portfolio/designer.html')


def dev_frontend(request):
    return render(request, 'portfolio/dev_frontend.html')


def dev_games(request):
    return render(request, 'portfolio/dev_games.html')


def editor_videos(request):
    return render(request, 'portfolio/editor_videos.html')


def projetista(request):
    return render(request, 'portfolio/projetista.html')


def rotinas_adm(request):
    return render(request, 'portfolio/rotinas_adm.html')


def obrigado(request):
    return render(request, 'portfolio/obrigado.html')


def desenvolvimento_web(request):
    return render(request, 'portfolio/desenvolvimento_web.html')


def html5(request):
    return render(request, 'portfolio/html5.html')


def css3(request):
    return render(request, 'portfolio/css3.html')


def design_mecanico(request):
    return render(request, 'portfolio/design_mecanico.html')


def autocad_base(request):
    return render(request, 'portfolio/autocad_base.html')


def autocad_3dcivil(request):
    return render(request, 'portfolio/autocad_3dcivil.html')


def autocad_mecanica_base(request):
    return render(request, 'portfolio/autocad_mecanica_base.html')


def autocad_projeto_civil(request):
    return render(request, 'portfolio/autocad_projeto_civil.html')


def solidworks(request):
    return render(request, 'portfolio/solidworks.html')


def revit_base(request):
    return render(request, 'portfolio/revit_base.html')


def sketchup(request):
    return render(request, 'portfolio/sketchup.html')


def design_grafico(request):
    return render(request, 'portfolio/design_grafico.html')


def dsmax(request):
    return render(request, 'portfolio/3dsmax.html')


def after_effects(request):
    return render(request, 'portfolio/after_effects.html')


def corel_draw(request):
    return render(request, 'portfolio/corel_draw.html')


def express(request):
    return render(request, 'portfolio/express.html')


def illustrator(request):
    return render(request, 'portfolio/illustrator.html')


def indesign(request):
    return render(request, 'portfolio/indesign.html')


def photoshop(request):
    return render(request, 'portfolio/photoshop.html')


def photoshop_fotografia(request):
    return render(request, 'portfolio/photoshop_fotografia.html')


def premiere_pro(request):
    return render(request, 'portfolio/premiere_pro.html')


def construct(request):
    return render(request, 'portfolio/construct.html')


def edicao_youtube(request):
    return render(request, 'portfolio/edicao_youtube.html')


def informatica(request):
    return render(request, 'portfolio/informatica.html')


def informatica_kids(request):
    return render(request, 'portfolio/informatica_kids.html')


def informatica_adultos(request):
    return render(request, 'portfolio/informatica_adultos.html')


def internet(request):
    return render(request, 'portfolio/internet.html')


def inteligencia_artificial(request):
    return render(request, 'portfolio/inteligencia_artificial.html')


def logica_programacao(request):
    return render(request, 'portfolio/logica_programacao.html')


def windows(request):
    return render(request, 'portfolio/windows.html')


def marketing(request):
    return render(request, 'portfolio/marketing.html')


def marketing_iniciantes(request):
    return render(request, 'portfolio/marketing_iniciantes.html')


def marketing_pessoal(request):
    return render(request, 'portfolio/marketing_pessoal.html')


def pacote_office(request):
    return render(request, 'portfolio/pacote_office.html')


def word(request):
    return render(request, 'portfolio/word.html')


def word_avancado(request):
    return render(request, 'portfolio/word_avancado.html')


def power_point(request):
    return render(request, 'portfolio/power_point.html')


def excel(request):
    return render(request, 'portfolio/excel.html')


def access(request):
    return render(request, 'portfolio/access.html')


def profissionais(request):
    return render(request, 'portfolio/profissionais.html')


def administracao(request):
    return render(request, 'portfolio/administracao.html')


def atendimento_cliente(request):
    return render(request, 'portfolio/atendimento_cliente.html')


def balconista_farmacia(request):
    return render(request, 'portfolio/balconista_farmacia.html')


def montagem_curriculo(request):
    return render(request, 'portfolio/montagem_curriculo.html')


def contabilidade(request):
    return render(request, 'portfolio/contabilidade.html')


def departamento_pessoal(request):
    return render(request, 'portfolio/departamento_pessoal.html')


def digitacao(request):
    return render(request, 'portfolio/digitacao.html')


def empreendedorismo(request):
    return render(request, 'portfolio/empreendedorismo.html')


def emprego_20(request):
    return render(request, 'portfolio/emprego_20.html')


def gestao_qualidade(request):
    return render(request, 'portfolio/gestao_qualidade.html')


def lideranca_gestao(request):
    return render(request, 'portfolio/lideranca_gestao.html')


def logistica(request):
    return render(request, 'portfolio/logistica.html')


def operador_caixa(request):
    return render(request, 'portfolio/operador_caixa.html')


def oratoria(request):
    return render(request, 'portfolio/oratoria.html')


def secretariado(request):
    return render(request, 'portfolio/secretariado.html')


def tecnicas_redacao(request):
    return render(request, 'portfolio/tecnicas_redacao.html')


def telemarketing(request):
    return render(request, 'portfolio/telemarketing.html')


def vendas(request):
    return render(request, 'portfolio/vendas.html')


def matematica_financeira(request):
    return render(request, 'portfolio/matematica_financeira.html')


def pacotes(request):
    return render(request, 'portfolio/pacotes.html')


def profissionalizante(request):
    return render(request, 'portfolio/profissionalizante.html')


def autocad_total(request):
    return render(request, 'portfolio/autocad_total.html')


def excel_total(request):
    return render(request, 'portfolio/excel_total.html')


def excel_dashboard(request):
    return render(request, 'portfolio/excel_dashboard.html')


def inteligencia_emocional(request):
    return render(request, 'portfolio/inteligencia_emocional.html')
