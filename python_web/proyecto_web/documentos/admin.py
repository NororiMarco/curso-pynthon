# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


# Register your models here.
from Documentos.models import Documento 

class DocumentoAdmin(admin.ModelAdmin):
	model = DocumentoAdmin

admin.site.register(Documento.DocumentoAdmin)
