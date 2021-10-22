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
    nome_mae = models.CharField(max_length=50, null=True, blank=True,verbose_name="Nome da Mãe")
    naturalidade = models.CharField(max_length=50, null=True ,blank=True)
    endereco = models.CharField(max_length=100, null=True ,blank=True,verbose_name="Endereço")
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    telefone = models.CharField(max_length=20, null=True,blank=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    TIPO_CHOICES = (
        ("rotina", "Rotina"),
        ("pronto_atendimento", "Pronto Atendimento"),
        ("acompanhamento", "Acompanhamento"),
    )
    sintomas = models.CharField(max_length=1000, null=False)
    tipo = models.CharField(max_length=20, null=False, choices=TIPO_CHOICES)
    especialidade = models.CharField(max_length=50, null=False)
    medico = models.CharField(max_length=500, null=False)
    telefone = models.CharField(max_length=20, null=True,blank=True)
    dataconsulta = models.DateField(null=False, verbose_name="Data da Consulta")
    dataretorno = models.DateField(null=True, blank=True, verbose_name="Data do Retorno")
    arquivo1 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo2 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo3 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo4 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo5 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo6 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo7 = models.FileField(null=True,blank=True,upload_to='images')
    evolucao_tratamento = models.CharField(max_length=1000, null=True,blank=True,verbose_name="Evolução do Tratamento")
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)


    def __str__(self):
        return self.sintomas
        #return self.especialidade

from django.db import models

# Create your models here.
