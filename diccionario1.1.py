import argparse


if __name__=='__main__':
    parser=argparse.ArgumentParser('Esto es una descripcion')
    parser.add_argument('nombre', help='el nombre de estudiante')
    parser.add_argument('edad')
    parser.add_argument('ciudad')
    parser.add_argument('curso')
    
    args = parser.parse_args()
    datos={
        'nombre':args.nombre,
        'edad':args.edad,
        'ciudad':args.ciudad,
        'curso':args.curso,
    }

    mensaje = 'El estudiante {nombre} con la edad de: {edad}, y que habita en la ciudad de {ciudad} y cursa el {curso} anio'

    print mensaje.format(nombre='asdf', edad='asdf' , ciudad='asdf',curso='asdf')
    for llave,valor in datos.iteritems():
        print llave,valor
