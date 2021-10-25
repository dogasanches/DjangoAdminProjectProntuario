from django.contrib import admin
from .models import Consulta, Paciente
from daterange_filter.filter import DateRangeFilter
#from .models import *

# Register your models here.

#admin.site.register(Paciente)
#admin.site.register(Consulta)

@admin.register(Consulta)
class ConsultaAdmin (admin.ModelAdmin):
    list_display = ("Paciente",'sintomas','tipo','especialidade','dataconsulta','arquivo1','arquivo2','arquivo3',)
    search_fields = ("sintomas",)
    list_filter = (
        ('dataconsulta',DateRangeFilter),
    )
    date_hierarch = ('dataconsulta')

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nome",'data_nascimento',)
    search_fields = ("nome",)
    list_filter = ('nome',)
    date_hierarch = ('nome')
