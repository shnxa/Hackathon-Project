from django.core.mail import send_mail
from decouple import config

def send_confirmation_mail(user, code):
    send_mail(
        subject='Письмо активации OnlineBook',
        message='Чтобы активировать аккаунт нужно ввести данный код:'
        f'\n\n{code}\n'
        f'\nНикому не передавайте данный код!'
        '\n\n\nOnline Book Web',
        from_email=config('EMAIL_USER'),
        recipient_list=[user],
        fail_silently=False,
    )