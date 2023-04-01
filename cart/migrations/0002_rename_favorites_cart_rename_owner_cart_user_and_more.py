# Generated by Django 4.1.7 on 2023-03-31 08:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favorites',
            new_name='Cart',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='owner',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'product')},
        ),
    ]