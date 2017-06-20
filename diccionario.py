import argparse


if __name__=='__main__':
    parser=argparse.ArgumentParser('Esto es una descripcion')
    parser.add_argument('--nombre', help='el nombre de estudiante')
    parser.add_argument('--apellido')
    parser.add_argument('--edad', type=int)
 	
    args = parser.parse_args()
    datos={
 	    'nombre':args.nombre,
 	    'apellido':args.apellido,
 	    'edad':args.edad,
	}

    for llave,valor in datos.iteritems():
        print llave,valor