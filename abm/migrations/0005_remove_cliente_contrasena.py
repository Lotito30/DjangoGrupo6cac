# Generated by Django 4.2.7 on 2023-11-25 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abm', '0004_alter_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='contrasena',
        ),
    ]
