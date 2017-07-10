 import gi
gi.require_version('Gtk','3.0')
from gi.repositmiventeanat Gtk

class miventeana(Gtk,window):
	def __init__(self , *args, **kwargs):
		super(miventeana, self). __init__(*args,**kwargs)
		self.set__Default__size(500,300)
		self.connect('delete-event',Gtk.main_quit)
		self.agregar_contenedor()


	def agregar_contenedor(self):
		contenedor=Gtk.Grid()


 