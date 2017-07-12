import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class Miventana(Gtk. Window):
	def __init__(self , *args, **kwargs):
		super(Miventana, self). __init__(*args,**kwargs)
		self.set__default__size(500,300)
		self.connect('delete-event',Gtk.main_quit)
		self.agregar_contenedor()
		self.agregar_entrada()
		self.agregar_boton()

	def agregar_contenedor(self):
	    self.contenedor=Gtk.Grid()
	    self.contenedor=set_column_homogeneous(True)
	    self.add(self.contenedor)
 
	def agregar_boton(self):
		self.agregar_boton =Gtk.Button('inicio')
		self.contenedor.attach_next_to(
		self.boton,
		self.entrada,
		Gtk.PositionType.BOTTON,
		1,
		1

		)

		self.boton.connect('clicked',self.agregar_fila)

	def agregar_entrada(self):
            self.entrada=Gtk.Entry()
            self.contenedor.attach(self.entrada,0,0,1,1)
  
        def Label(self):
    	    etiqueta =Gtk.Label()
    	    etiqueta.set_markup('texto a ingresar')

        if __name__=='main':
    	    ventana =Miventana()
    	    ventana.show_all()

    	    Gtk.main()

     
     
