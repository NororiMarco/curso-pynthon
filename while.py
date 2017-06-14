import argparse
Jugador_1= 0
Computadora=0

print ("Vamos a jugar Piedra, papel y tijera" "(^-^/) ")
print ("1-piedra")
print ("2-papel")
print ("3-tijera")
opcion =str(input("Que deseas elegir"))

if opcion==1:
	jugadorelige= "piedra"
elif opcion==2:
	jugadorelige= "papel"
elif opcion==3:
	jugadorelige= "tijera"
	print ("Jugador elige",jugadorelige)
	print ("Presiona 0 para que computadora eliga  (^-^/) ")
	
if opcion==0:
   Computadoraelige = random.ramdrange(" Piedra", "Papel","tijera" )
print ("Computadora elige",Computadoraelige)

print()