# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import View
#
from django.shortcuts import render
##crear vista de documentos -definir metodo get
from documentos.models import Documento
class documentos(views):
	"""docstring for ClassName"""

	def get(self, request, *args, **kwargs):
		docs = Documento.objects.all()
		#Select *From documentos_Documento;
		context = {
		    'docs':docs,
		    'encabezado':'Mis documentos'
		}
 
		return render(request,
			'base.html',
		 context)



