# Generated by Django 5.1.1 on 2024-12-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_remove_cliente_marker'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='resultado_credito',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
