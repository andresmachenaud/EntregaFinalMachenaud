# Generated by Django 4.1.2 on 2022-12-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0012_rename_genero_libro_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='editado',
            field=models.DateField(null=True),
        ),
    ]
