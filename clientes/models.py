from django.db import models # type: ignore

class Cliente(models.Model):
    SEXO_CHOICES = [
        ('Man', 'Man'),
        ('Woman', 'Woman'),
    ]

    REGIAO_CHOICES = [
        ('Minsk region', 'Minsk region'),
        ('Gomel region', 'Gomel region'),
        ('Brest region', 'Brest region'),
        ('Mogilev region', 'Mogilev region'),
        ('Vitebsk region', 'Vitebsk region'),
        ('Grodno region', 'Grodno region'),
    ]


    ESTADO_CIVIL_CHOICES = [
        ('Married', 'Married'),
        ('Single/unmarried', 'Single/unmarried'),
        ('Divorced/widow', 'Divorced/widow'),
    ]

    NUMERO_FILHOS_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('More than 3', 'More than 3'),
    ]

    PROPRIEDADE_CHOICES = [
        ('property', 'property'),
        ('rented/hire', 'rented/hire'),
        ('other', 'other'),
    ]

    EDUCACAO_CHOICES = [
        ('Higher education (one or more)', 'Higher education (one or more)'),
        ('Secondary education (plus special education)', 'Secondary education (plus special education)'),
        ('Incomplete higher education', 'Incomplete higher education'),
        ('Primary or lower secondary education', 'Primary or lower secondary education'),
    ]

    VINCULO_EMPREGATICIO_CHOICES = [
        ('Work', 'Work'),
        ('Unemployed', 'Unemployed'),
        ('Pensioner', 'Pensioner'),
    ]

    FONTE_RENDA_CHOICES = [
        ('NE employee', 'NE employee'),
        ('Enterpreneur', 'Enterpreneur'),
        ('Head/Deputy head (division)', 'Head/Deputy head (division)'),
        ('Pensioner', 'Pensioner'),
        ('Head/Deputy head (organiz.)', 'Head/Deputy head (organiz.)'),
    ]

    sexo = models.CharField(max_length=5, choices=SEXO_CHOICES, default='Man')
    regiao = models.CharField(max_length=20, choices=REGIAO_CHOICES, default='Minsk region')
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES, default='Single')
    numero_filhos = models.CharField(max_length=15, choices=NUMERO_FILHOS_CHOICES, default='0')
    propriedade = models.CharField(max_length=15, choices=PROPRIEDADE_CHOICES, default='property')
    educacao = models.CharField(max_length=100, choices=EDUCACAO_CHOICES, default='Secondary education')
    vinculo_empregaticio = models.CharField(max_length=15, choices=VINCULO_EMPREGATICIO_CHOICES, default='Work')
    fonte_renda = models.CharField(max_length=30, choices=FONTE_RENDA_CHOICES, default='NE employee')
    marker = models.BooleanField(default=False)  # Coluna alvo para classificação de empréstimos

    def __str__(self):
        return f"{self.sexo} - {self.regiao} - {self.estado_civil}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
