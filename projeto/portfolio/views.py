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


