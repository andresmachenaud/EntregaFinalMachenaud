# Generated by Django 4.1.2 on 2022-12-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLogin', '0005_alter_perfil_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
