palabras = ['perro']
adivina = [[]for x in range(len(palabras[0]))] 
print(adivina)
def resultado(palabra, letra):
    contador = 0
    for x in palabra:
        if x == letra:
            adivina[contador] = '['+x+']'
        contador += 1

light = True
while light:
    ent=str(input('letra: '))
    elegida=palabras[0]
    if ent in elegida:
        resultado(elegida, ent)
        print(", ".join(map(str,adivina)).replace(",","",-1))
    elif ent == '6':
        light = False
    else:
        print("otro intento")

def menu():
    entrada = str(input('Seleccione una opcion\n1. Jugar\n2. Cambiar parametros\n3. Mostrar resultados\n4. Ayuda\n5. Acerca de...\n6. Salir\nOpcion: '))
    if entrada == '1':
        print('trabajando en ello')
        #jugar al jogo
        return True
    elif entrada == '2':
        print('trabajando en ello')
        #cambiar pool de palabras
        return True
    elif entrada == '3':
        print('trabajando en ello')
        #mostrar cantidad de partidas ganadas
        return True
    elif entrada == '4':
        print('trabajando en ello')
        #mostrar instrucciones del juego
        return True
    elif entrada == '5':
        print('trabajando en ello')
        #info de creadores y anno de creacion
        return True
    elif entrada == '6':
        #salir del programa
        return False 
#salida = True
#while salida:
    #salida = menu()