from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Material  # Подключаем модель

# Главная страница
def home(request):
    materials = Material.objects.all()  # Загружаем все материалы из базы
    return render(request, 'landing/index.html', {'materials': materials})

# Форма обратной связи
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if name and email and message:
            send_mail(
                f'Сообщение от {name}',
                message,
                email,
                ['yulianov76@mail.ru'],  # Email компании
                fail_silently=False,
            )
            messages.success(request, "Ваше сообщение отправлено!")
            return redirect('contact')

    return render(request, 'landing/contact.html')  # Исправленный путь к шаблону
