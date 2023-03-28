# Generated by Django 4.1.7 on 2023-03-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('modelo', models.IntegerField(verbose_name='Modelo')),
                ('color', models.CharField(max_length=20, verbose_name='Color')),
            ],
            options={
                'db_table': 'auto',
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apelido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]
