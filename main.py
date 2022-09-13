import time 
import random
puntaje = 0
iniciar_trivia = True
intentos = 0
nombre = input("ingresa tu nombre: ")
puntaje =random.randint(0, 10)
time.sleep(1)
print("\n hola",'\033[32m'+nombre+'\033[39m')
print('\033[33m'+"bienvenido a mi trivia sobre astronomia"+'\033[39m')
print('\033[33m'+"queremos saber cuanto sabes del universo"+'\033[39m')
print('\033[33m'+"tienes",puntaje, "puntos"+'\033[39m')
print('\033[33m'+"responde las 3 preguntas escribiendo la alternativa correcta y presiona ´enter´ para enviar tu respuesta:\n"+'\033[39m')

for numero_carga in range (3, 0, -1):
 print (numero_carga)
 time.sleep(1)
while iniciar_trivia == True:
  intentos +=1
  puntaje = 0
  print ("\nintento numero:", intentos )
  input("presiona enter para continuar")
  print('\033[36m'+"1) ¿cuantos satelites tiene jupiter?"+'\033[39m')
  print("a) 70")
  print("b) 79")
  print("c) 82")
  print("d) 81") 
  respuesta_1 = input("\ntu respuesta: ")
  while respuesta_1 not in ("a","b","c","d","x"):
    respuesta_1 = input("debes responder a,b,c o d.INGRESA NUEVAMENTE TU  RESPUESTA: ")
  if respuesta_1 == "a":
    puntaje -=random.randint(0, 5)
    print('\033[31m'+"incorrecto!", nombre , "jupiter no tiene 70 satelites"+'\033[39m')
    print("tienes",puntaje,"puntos\n")
  elif respuesta_1 == "x":
    puntaje +=20
    print(nombre,"este es un mensaje secreto, En la mitología griega y romana, Júpiter ocultaba sus travesuras gracias a un velo de nubes que confeccionaba a su alrededor. Pero Juno, reina de los dioses y a su vez hermana y esposa de Júpiter, fue capaz de mirar a través de dichas nubes y revelar la verdadera personalidad del dios.")
    print("tienes",puntaje,"puntos\n")
  elif respuesta_1 == "c":
    puntaje -=random.randint(0, 5)
    print('\033[31m'+"incorrecto!", nombre, "jupiter no tiene 82 satelites"+'\033[39m' )
    print("tienes",puntaje,"puntos\n")
  elif respuesta_1 == "d":
    puntaje -=random.randint(0, 5)
    print('\033[31m'+"incorrecto" , nombre , "jupiter no tiene 81 satelites"+'\033[39m')
    print("tienes",puntaje,"puntos\n")
  else:
    puntaje +=random.randint(0, 10)
    print ("muy bien", nombre, "!")
    print("tienes",puntaje,"puntos\n")
  time.sleep(1)
  print('\033[36m'+ "2)¿cual es la edad  del sol ?"+'\033[39m')
  print("a) 4,603 miles de millones de años ")
  print("b) 5,710 miles de millones de años ")
  print("c) 3,900 miles de millones de años ")
  print("d) 5,204 miles de millones de años ")
  respuesta_2 = input("\ntu repuesta: ")
  while respuesta_2 not in ("a","b","c","d","x"):
    respuesta_2 = input("debes responder a,b,c o d.INGRESA NUEVAMENTE TU  RESPUESTA: ")
  if respuesta_2 == "b":
    puntaje -=random.randint(0, 5)
    print('\033[31m'+"incorrecto", nombre , "el sol no es tan viejo "+'\033[39m')
    print("tienes",puntaje,"puntos\n")
  elif respuesta_2 == "x":
    puntaje +=20
    print(nombre , "este es un mensaje secreto, el astro atravesó una fase,  llamada   Mínimo Solar, lo que implicaba una  “menor presencia  de manchas solares” y por consecuencia menos actividad, pero que no provocaría una baja extrema en la temperatura de la Tierra.")
    print("tienes",puntaje,"puntos\n")
  elif respuesta_2 == "c":
    puntaje -=random.randint(0, 5)
    print('\033[31m'+"incorrecto", nombre ," el sol no es tan joven "+'\033[39m')
    print("tienes",puntaje,"puntos\n")
  elif respuesta_2 == "d":
    puntaje -=random.randint(0, 5)
    print('\033[31m'+"incorrecto", nombre , "el sol no es tan viejo"+'\033[39m')
    print("tienes",puntaje,"puntos\n")
  else:
    puntaje +=random.randint(0, 10)
    print("excelente", nombre , "!")
    print("tienes",puntaje,"puntos\n")
  time.sleep(1)
  print('\033[36m'+"3) ¿que planeta gira al revés del sol ?"+'\033[39m')
  print("a) mercurio ")
  print("b) jupiter ")
  print("c) marte ")
  print("d) venus ")
  respuesta_3 = input("\ntu respuesta: ")
  while respuesta_3 not in ("a","b","c","d","x"):
    respuesta_3 = input("debes responder a,b,c o d.INGRESA NUEVAMENTE TU  RESPUESTA: ")
  if respuesta_3 == "a":
    puntaje -=random.randint(0, 5)
    print('\033[31m'+"incorrecto!", nombre ,"mercurio gira en sentido antihorario"+'\033[39m' )
    print("tienes",puntaje,"puntos\n")
  elif respuesta_3 == "x":
    puntaje +=20
    print(nombre,"este es un mensaje secreto,El Lucero del alba, a veces llamado´Estrella del alba´, es una denominación popular para referirse al planeta Venus")
    print("tienes",puntaje,"puntos\n")
  elif respuesta_3 == "b":
    puntaje -=random.randint(0, 5)
    print('\033[31m'+"incorrecto", nombre,"jupiter gira en sentido antihorario"+'\033[39m')
    print("tienes",puntaje,"puntos\n")
  elif respuesta_3 == "c":
    puntaje -=random.randint(0, 5)
    print('\033[31m'+"incorrecto", nombre ,"marte gira en sentido antihorario"+'\033[39m')
    print("tienes",puntaje,"puntos\n")
  else:
    puntaje +=random.randint(0, 10)
    print("CORRECTO",nombre ,"!")
    print("tienes",puntaje,"puntos\n")
  time.sleep(1)
  print('\033[36m'+"4)¿cuantos planetas hay en nuestro sistema solar?"+'\033[39m')
  print("a) 9")
  print("b) 8")
  print("c) 10")
  print("d) 2")
  respuesta_4 = input("\ntu repuesta: ")
  while respuesta_4  not in ("a","b","c","d"):
   respuesta_4 = input("debes responder a , b , c ,d.ingresa nuevamente tu respuesta")
  if respuesta_4 == "a":
    print('\033[31m'+"incorrecto"+'\033[39m')
    puntaje =puntaje +5
  elif respuesta_4 =="c":
    print('\033[31m'+"totalmente incorrecto"+'\033[39m')
    puntaje =puntaje -5
  elif respuesta_4 == "d":
    print('\033[31m'+"muy mal"+'\033[39m')
    puntaje =puntaje /2
  else:
    print(" muy bien ")
    puntaje =puntaje *2
  print('\033[32m'+"\nGRACIAS",nombre,"POR JUGAR MI TRIVIA, ALCANZASTE",puntaje,"PUNTOS"+'\033[39m')
  print("\n¿deseas intentar mi trivia nuevamente?")
  repetir_trivia = input ("ingresa 'si'para repetir o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":
   print("\nespero" , nombre, "lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False