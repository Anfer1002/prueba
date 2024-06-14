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