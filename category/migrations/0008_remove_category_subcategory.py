# Generated by Django 4.1.7 on 2023-04-01 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_alter_category_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
    ]
