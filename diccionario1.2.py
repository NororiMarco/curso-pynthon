import random

NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]

def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes[nombre] = {
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'cuidad': random.choice(CIUDADES)
        }

    return estudiantes
if __name__ == '__main__':
	diccionario = generar_diccionario_estudiantes()
	for llave,valor in diccionario.iteritems():
		print llave,valor


mensaje = 'El estudiante llamado {nombre} con la edad de: {edad}, y que habita en la ciudad de {ciudad} y cursa el {curso} de la Universidad '

    
    for llave,valor in datos.iteritems():
        print mensaje.format(datos)

