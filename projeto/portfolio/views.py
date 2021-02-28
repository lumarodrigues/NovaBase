from django.shortcuts import render
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
            send_mail('Mensagem de ' + name, message + '\n\nTelefone: ' + phone + '\n\nEmail: ' + email,
                      [EMAIL_USER], [EMAIL_USER], fail_silently=False,)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Email successfully sent!')

    return render(request, 'portfolio/home.html')

def autocad(request):
    return render(request, 'portfolio/autocad.html')


def operador(request):
    return render(request, 'portfolio/operador.html')


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


def excel(request):
    return render(request, 'portfolio/excel.html')


def profissionalizante(request):
    return render(request, 'portfolio/profissionalizante.html')


def projetista(request):
    return render(request, 'portfolio/projetista.html')


def rotinas_adm(request):
    return render(request, 'portfolio/rotinas_adm.html')
