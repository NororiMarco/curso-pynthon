import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class miventeana(Gtk,window):
	def __init__(self , *args, **kwargs):
		super(miventana, self). __init__(*args,**kwargs)
		self.set__Default__size(500,300)
		self.connect('delete-event',Gtk.main_quit)
		self.agregar_contenedor()


	def agregar_contenedor(self):
		contenedor=Gtk.Grid()
		contenedor=

	#def agregar_contenedor(self):
		#contenedor=Gtk.Grid()
		#contenedor=

		text =Gtk.Entry(text= "hola")
		boton =Gtk.Button('boton')
		label=Gtk.lable('nada que poner')

if __name__	=='__main__':
	ventana=Mi_ventana()
	ventana=add(text)
	ventana=add(label)
	ventana=show()

	Gtk.main()

 