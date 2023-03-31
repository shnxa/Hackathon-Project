from django.core.mail import send_mail


def send_confirmation_mail(user, code):
    send_mail(
        subject='Письмо активации ShopAPI',
        message='Чтобы активировать аккаунт нужно ввести данный код:'
        f'\n\n{code}\n'
        f'\nНикому не передавайте данный код!'
        '\n\n\nSHOP API Test Build',
        from_email='shop.api.email@gmail.com',
        recipient_list=[user],
        fail_silently=False,
    )