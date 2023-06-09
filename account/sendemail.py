from django.core.mail import send_mail
from decouple import config

def send_confirmation_mail(user, code):
    send_mail(
        subject='Письмо активации | OnlineBook',
        message='Чтобы активировать аккаунт нужно ввести данный код:'
        f'\n\n{code}\n'
        f'\nНикому не передавайте данный код!'
        '\n\n\nOnline Book Web',
        from_email=config('EMAIL_USER'),
        recipient_list=[user],
        fail_silently=False,
    )

def send_password_reset_mail(user, code):
    send_mail(
        subject='Письмо для сброса пароля | OnlineBook',
        message='Чтобы приступить к процессу сброса пароля нужно ввести данный код:'
                f'\n\n{code}\n'
                f'\nНикому не передавайте данный код!'
                '\n\n\nOnline Book Web',
        from_email=config('EMAIL_USER'),
        recipient_list=[user],
        fail_silently=False,
    )

def password_change_notification(user):
    send_mail(
        subject='Сброс пароля | OnlineBook',
        message="Ваш пароль был успешно изменен!",
        from_email=config('EMAIL_USER'),
        recipient_list=[user],
        fail_silently=False,
    )