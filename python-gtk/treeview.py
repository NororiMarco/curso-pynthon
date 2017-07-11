import gi
gi.require_version('Gtk','3.0')
from gi.repository Mi_ventana import Gtk


class miventeana(Gtk,window):
	def __init__(self , *args, **kwargs):
		super(miventana, self). __init__(*args,**kwargs)
		self.set__Default__size(500,300)
		self.connect('delete-event',Gtk.main_quit)
		self.agregar_contenedor()

def agregar_contenedor(self):
		contenedor=Gtk.Grid()
		contenedor=#falta 

##copiado del profesor
def agregar_contenedor(self):
	self.contenedor=Gtk.Grid()
	self.contenedor=set_column_homogeneous(True)
	self.add(self.contenedor)

def agregar_entrada(self)
    self.entrada=Gtk.Entry()
    self.contenedor=(falta)





    ###pasos para crear treview
    #def agreagar_lista(self)
    ###crea un treeview
    #1-crear el model de datos Gtk.ListStorage(type,type...type)
    #2-crear el widget que contiene o muestra los datos de modelo treeview (<model>)
    #3-Definir las columnas y su contenido
    #3.1-crea celda para cada columna de la fila. Los cellRenderer son widget dependiendo de tipo
    #3.2- crear columnas(treeviewcolumn) del treeview que mostraran los datos usando callReenderer widget como elemento hijo
    #arg: (titulo, callReenderer, posicion en le modelo de la info a mostrar)
    #3.3- agregar cada treeviewcolumn al treeview widget 