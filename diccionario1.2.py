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
            'curso': random.randrange(1, 5),
            'ciudad': random.choice(CIUDADES)
        }

    return estudiantes
if __name__ == '__main__':
	diccionario = generar_diccionario_estudiantes()
	for llave,valor in diccionario.iteritems():
		print llave,valor

print ''
print 'UNIVERSIDAD DE MANAGUA'
print 'el mas alto nivel'
print ''
print 'Registro de estudiantes '
print''
mensaje = 'El estudiante llamado(a) {nombre} con la edad de: {edad}, y que habita en la ciudad de {ciudad} y esta en el curso numero {curso} de la Universidad '
print ''
print 'Inciso numero 1'
for nombre_estudiante, datos in diccionario.iteritems():
        print mensaje.format(nombre=nombre_estudiante, edad=datos['edad'], ciudad=datos['ciudad'],curso=datos['curso'])
print ''
print 'Inciso numero 2(estudiantes de Managua )'
for nombre_estudiante, datos in diccionario.iteritems():
    if datos['ciudad']  =='Managua':
        print mensaje.format(nombre=nombre_estudiante, edad=datos['edad'], ciudad=datos['ciudad'],curso=datos['curso'])

print''
print 'Inciso numero 3(estudiantes de masaya y en el curso 1)'
for nombre_estudiante, datos in diccionario.iteritems():
    if datos['ciudad']  =='Masaya' and datos['curso']== 1:
        print mensaje.format(nombre=nombre_estudiante, edad=datos['edad'], ciudad=datos['ciudad'],curso=datos['curso'])

print ''
print 'Inciso numero 4(estudiantes menores de 21)'
for nombre_estudiante, datos in diccionario.iteritems():
    if datos['edad'] <21:
        print mensaje.format(nombre=nombre_estudiante, edad=datos['edad'], ciudad=datos['ciudad'],curso=datos['curso'])

