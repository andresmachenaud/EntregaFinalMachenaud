# Generated by Django 4.1.2 on 2022-12-15 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0011_alter_mensaje_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='genero',
            new_name='categoria',
        ),
    ]
