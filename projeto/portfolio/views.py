from django.shortcuts import render
from django.core.mail import send_mail

from projeto.forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        send_mail(

            'Mensagem de ' + name,
            message + '\nTelefone: ' + phone,
            email,
            ['rdsluma@gmail.com'],

        )
        return render(request, 'portfolio/home.html', {})
    else:
        return render(request, 'portfolio/home.html', {})


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
