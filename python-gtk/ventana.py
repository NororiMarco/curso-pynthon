import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

if __name__=='__main__':
	ventana = Gtk.Window(title = 'ejemplo 1')
	ventana.connect('delete-event',Gtk.main_quit)
	boton = Gtk.Button('boton 1')
	boton2 = Gtk.Button('boton 2')
	boton3 = Gtk.Button('boton 3')
	boton4 = Gtk.Button('boton 4')
	contenedor = Gtk.Grid()
	contenedor.set_column_homogeneous(True)
	contenedor.set_row_homogeneous(False)

	contenedor.attach(
		boton,#elemento
		0, #columna
		0, #fila
		3, #n columna a usar
		1, #n filas a usar 
		)
	contenedor.attach(boton2,1,1,1,1)
	contenedor.attach(boton3,2,1,1,1)
	contenedor.attach(boton4,0,2,1,1)

	ventana.add(contenedor)
	contenedor = Gtk.VBox()
	contenedor.pack_start(boton, False,False,0)
	contenedor.pack_end(boton2, False,False,0)
	ventana.add(contenedor)
	ventana.show_all()

	Gtk.main()

