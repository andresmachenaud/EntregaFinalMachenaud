# Generated by Django 4.1.2 on 2022-12-13 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0004_alter_libro_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AppBlog.libro'),
        ),
    ]
