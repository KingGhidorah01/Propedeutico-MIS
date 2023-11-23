def cuenta(cadena, letraBuscar):
    cuenta = 0
    for letra in cadena:
        if letra == letraBuscar:
            cuenta = cuenta + 1
    #print(cuenta)


cuenta("banana", "n")


identificador = open('mbox-short.txt')
contador = 0
for linea in identificador:
    contador = contador + 1
print('Contador de Lineas:', contador)

identificador = open('mbox-short.txt')
entrada = identificador.read()
print(len(entrada))
print(entrada[:20])

identificador = open('mbox-short.txt')
for linea in identificador:
    if linea.startswith('From:'):
        print(linea)


identificador = open('mbox-short.txt')
for linea in identificador:
 linea = linea.rstrip()
# Salta 'lineas sin interes'
 if not linea.startswith('From:'):
     continue
# Procesa nuestra 'linea de interes’
 print(linea)