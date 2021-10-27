# Create your models here.
from django.db import models


# Create your models here.

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    TIPO_CHOICES = (
        ("rotina", "Rotina"),
        ("pronto_atendimento", "Pronto Atendimento"),
        ("acompanhamento", "Acompanhamento"),
        ("medicamento uso contínuo", "Medicamento uso Contínuo"),
        ("vacinação", "Vacinação"),
    )
    tipo = models.CharField(max_length=24, null=False, choices=TIPO_CHOICES)
    dataconsulta = models.DateField(null=False, verbose_name="Data da Consulta")
    especialidade = models.CharField(max_length=50, null=True,blank=True)
    medico = models.CharField(max_length=500, null=True,blank=True)
    crm = models.CharField(max_length=500, null=True,blank=True,verbose_name="CRM")
    telefone = models.CharField(max_length=20, null=True,blank=True)
    models.CharField(max_length=100, null=True, blank=True, verbose_name="Endereço")
    sintomas = models.CharField(max_length=1000, null=False,verbose_name="Sintomas / Motivo")
    diagnostico = models.CharField(max_length=1000, null=True,blank=True)
    medicamento = models.CharField(max_length=1000, null=True,blank=True)
    evolucao_tratamento = models.CharField(max_length=1000, null=True,blank=True,verbose_name="Evolução do Tratamento")
    dataretorno = models.DateField(null=True, blank=True, verbose_name="Data do Retorno")
    arquivo1 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo2 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo3 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo4 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo5 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo6 = models.FileField(null=True,blank=True,upload_to='images')
    arquivo7 = models.FileField(null=True,blank=True,upload_to='images')
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.sintomas
        #return self.especialidade

from django.db import models

# Create your models here.
