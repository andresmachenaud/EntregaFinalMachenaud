# Generated by Django 4.1.2 on 2022-12-18 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppLogin', '0007_alter_perfil_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='imagen',
            new_name='avatar',
        ),
    ]
