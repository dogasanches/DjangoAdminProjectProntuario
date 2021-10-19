# Create your models here.
from django.db import models


# Create your models here.

class Paciente(models.Model):
    SEXO_CHOICES = (
        ("feminino", "Feminino"),
        ("masculino", "Masculino"),
    )
    nome = models.CharField(max_length=50, null=False)
    data_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento")
    nome_mae = models.CharField(max_length=50, null=False)
    naturalidade = models.CharField(max_length=50, null=False)
    endereco = models.CharField(max_length=100, null=False)
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    telefone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nome

class Consultas(models.Model):
    TIPO_CHOICES = (
        ("rotina", "Rotina"),
        ("pronto atendimento", "Pronto Atendimento"),
        ("acompanhamento", "Acompanhamento"),
    )
    sintomas = models.CharField(max_length=500, null=False)
    tipo = models.CharField(max_length=20, null=False, choices=TIPO_CHOICES)
    especialidade = models.CharField(max_length=50, null=False)
    medico = models.CharField(max_length=500, null=False)
    telefone = models.IntegerField(null=False)
    data_consulta = models.DateField(null=False, verbose_name="Data da Consulta")
    data_retorno = models.DateField(null=False, verbose_name="Data do Retorno")
    arquivo_1 = models.FileField(upload_to='images')
    arquivo_2 = models.FileField(upload_to='images')
    arquivo_3 = models.FileField(upload_to='images')
    arquivo_4 = models.FileField(upload_to='images')
    arquivo_5 = models.FileField(upload_to='images')
    arquivo_6 = models.FileField(upload_to='images')
    arquivo_7 = models.FileField(upload_to='images')
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    evolucao_tratamento = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.especialidade


from django.db import models

# Create your models here.
