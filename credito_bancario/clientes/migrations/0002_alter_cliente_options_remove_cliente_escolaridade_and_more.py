# Generated by Django 5.1.3 on 2024-11-10 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='escolaridade',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nome',
        ),
        migrations.AddField(
            model_name='cliente',
            name='educacao',
            field=models.CharField(choices=[('Higher education (one or more)', 'Higher education (one or more)'), ('Secondary education (plus special education)', 'Secondary education (plus special education)'), ('Incomplete higher education', 'Incomplete higher education'), ('Primary or lower secondary education', 'Primary or lower secondary education')], default='Secondary education', max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='estado_civil',
            field=models.CharField(choices=[('Married', 'Married'), ('Single/unmarried', 'Single/unmarried'), ('Divorced/widow', 'Divorced/widow')], default='Single', max_length=20),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fonte_renda',
            field=models.CharField(choices=[('NE employee', 'NE employee'), ('Enterpreneur', 'Enterpreneur'), ('Head/Deputy head (division)', 'Head/Deputy head (division)'), ('Pensioner', 'Pensioner'), ('Head/Deputy head (organiz.)', 'Head/Deputy head (organiz.)')], default='NE employee', max_length=30),
        ),
        migrations.AddField(
            model_name='cliente',
            name='marker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero_filhos',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('More than 3', 'More than 3')], default='0', max_length=15),
        ),
        migrations.AddField(
            model_name='cliente',
            name='propriedade',
            field=models.CharField(choices=[('property', 'property'), ('rented/hire', 'rented/hire'), ('other', 'other')], default='property', max_length=15),
        ),
        migrations.AddField(
            model_name='cliente',
            name='vinculo_empregaticio',
            field=models.CharField(choices=[('Work', 'Work'), ('Unemployed', 'Unemployed'), ('Pensioner', 'Pensioner')], default='Work', max_length=15),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='regiao',
            field=models.CharField(choices=[('Minsk region', 'Minsk region'), ('Gomel region', 'Gomel region'), ('Brest region', 'Brest region'), ('Mogilev region', 'Mogilev region'), ('Vitebsk region', 'Vitebsk region'), ('Grodno region', 'Grodno region')], default='Minsk region', max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('Man', 'Man'), ('Woman', 'Woman')], default='Man', max_length=5),
        ),
    ]
