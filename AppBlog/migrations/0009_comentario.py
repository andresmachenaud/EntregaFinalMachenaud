# Generated by Django 4.1.2 on 2022-12-15 01:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppLogin', '0005_alter_perfil_user'),
        ('AppBlog', '0008_alter_entrada_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuerpo', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppLogin.perfil')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlog.entrada')),
            ],
        ),
    ]
