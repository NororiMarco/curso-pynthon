
import random
import gi
#import logging


# importar modulo que contiene clase base de actividad.
#from sugar3.activity import activity

#from sugar3.graphics.toolbarbox import ToolbarBox

# boton para toolbar
#from sugar3.activity.widgets import (

    #ActivityToolbarButton,
    #StopButton
#)

#from ppt_utils import OPCIONES

#gi.require_version('Gtk', '3.0')
#from gi.repository import Gtk, Gdk, GdkPixbuf
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#logger = logging.getLogger(__name__)

#ventanas

class continentes(Gtk.Window):


	def __init__(self, *args, **kwargs):
		super(continentes, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
  		self.agregar_contenedor()
    		self.agregar_boton()
      		self.agregar_lista()



	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
  		self.add(self.contenedor)
		#self.set_canvas(self.contenedor)
		#self.agregar_boton
	def agregar_boton(self):
		self.boton = Gtk.Button('Europa')
  		self.contenedor.attach(self.boton,3,3,1,1)
		self.boton.connect('clicked',self.lista_capitales)
  		#self.boton2 = Gtk.Button('Europa')
  		#self.boton3 = Gtk.Button('Asia')
  	def agregar_lista(self):
		self.modelo = Gtk.ListStore(str)
		self.lista_pais = Gtk.TreeView(self.modelo)

  		pais_cellrenderer = Gtk.CellRendererText()
		columna_paises =  Gtk.TreeViewColumn(
		'Capitales de Europa',
		pais_cellrenderer,
		text=0)


		self.lista_pais.append_column(columna_paises)
  		self.contenedor.attach_next_to(self.lista_pais, self.boton, Gtk.PositionType.BOTTOM, 1,1)

#capitales de america
  	def lista_capitales(self,btn=None):
       		if len(self.modelo) == 0:
         		self.modelo.append(['Tirana']),
            self.modelo.append(['Berlin']),### problema de identacion 
            self.modelo.append(['Andorra La Vieja']),
            self.modelo.append(['Erevan']),
            self.modelo.append(['Viena']),
            self.modelo.append(['Baku']),
            self.modelo.append(['Bruselas']),
            self.modelo.append(['Minsk']),
            self.modelo.append(['Sarajevo']),
            self.modelo.append(['Sofia']),
            self.modelo.append(['Nicosia']),
            self.modelo.append(['Ciudad del Vaticano']),
            self.modelo.append(['Zagred']),
            self.modelo.append(['Copenhague']),
            self.modelo.append(['Bratislava']),
            self.modelo.append(['luibliana']),
            self.modelo.append(['Madrid']),
            self.modelo.append(['Tallin']),
            self.modelo.append(['Helsinki']),
            self.modelo.append(['Paris']),
            self.modelo.append(['Tiflis']),
            self.modelo.append(['Atenas']),
            self.modelo.append(['Budapest']),
            self.modelo.append(['Dublin']),
            self.modelo.append(['Reikiavik']),
            self.modelo.append(['Roma']),
            self.modelo.append(['Astana']),
            self.modelo.append(['Riga']),
            self.modelo.append(['Vaduz']),
            self.modelo.append(['Vilna']),
            self.modelo.append(['Luxemburgo']),
            self.modelo.append(['Skopie']),
            self.modelo.append(['La Valeta']),
            self.modelo.append(['Chisinau']),
            self.modelo.append(['Monaco']),
            self.modelo.append(['Podgorica']),
            self.modelo.append(['Oslo']),
            self.modelo.append(['Amsterdam']),
            self.modelo.append(['Varsovia']),
            self.modelo.append(['Lisboa']),
            self.modelo.append(['Londres']),
            self.modelo.append(['Praga']),
            self.modelo.append(['Bucarest']),
            self.modelo.append(['Moscu']),
            self.modelo.append(['San Marino']),
            self.modelo.append(['Belgrado']),
            self.modelo.append(['Esocolmo']),
            self.modelo.append(['Berna']),
            self.modelo.append(['Ankarna']),
            self.modelo.append(['Kiev']),
          


if __name__ == '__main__':
	ventana = continentes()
	ventana.show_all()

Gtk.main()