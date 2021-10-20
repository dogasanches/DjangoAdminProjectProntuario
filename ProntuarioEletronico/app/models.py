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
        ("pronto_atendimento", "Pronto_Atendimento"),
        ("acompanhamento", "Acompanhamento"),
    )
    sintomas = models.CharField(max_length=1000, null=False)
    tipo = models.CharField(max_length=20, null=False, choices=TIPO_CHOICES)
    especialidade = models.CharField(max_length=50, null=False)
    medico = models.CharField(max_length=500, null=False)
    telefone = models.IntegerField(null=False)
    dataconsulta = models.DateField(null=False, verbose_name="Data_da_Consulta")
    dataretorno = models.DateField(null=False, verbose_name="Data_do_Retorno")
    arquivo1 = models.FileField(upload_to='images')
    arquivo2 = models.FileField(upload_to='images')
    arquivo3 = models.FileField(upload_to='images')
    arquivo4 = models.FileField(upload_to='images')
    arquivo5 = models.FileField(upload_to='images')
    arquivo6 = models.FileField(upload_to='images')
    arquivo7 = models.FileField(upload_to='images')
    evolucao_tratamento = models.CharField(max_length=1000, null=False)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)


    def __str__(self):
        return self.especialidade


from django.db import models

# Create your models here.
