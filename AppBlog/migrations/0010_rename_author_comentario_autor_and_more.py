# Generated by Django 4.1.2 on 2022-12-15 02:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppLogin', '0005_alter_perfil_user'),
        ('AppBlog', '0009_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='created_date',
            new_name='fecha',
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppLogin.perfil')),
            ],
        ),
    ]
