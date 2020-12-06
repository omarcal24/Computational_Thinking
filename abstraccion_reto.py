# La idea es que el usuario elija la opcion que prefiera y después
# el numero al que le quiere sacar la raíz cuadrada


def enumeracion():
    objetivo = int(input('Escoge un numero para sacarle la raiz cuadrada: '))
    respuesta = 0
    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')


def busqueda_binaria():
    objetivo = int(input('Escoge un numero para sacarle la raiz cuadrada: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'la raiz cuadrada de {objetivo} es  {respuesta}')


def aproximacion():
    objetivo = int(input('Escoge un numero para sacarle la raiz cuadrada: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No encontramos la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


print('----------------------------------------------')
print('Bienvenidos al programa automatizado para sacar raices cuadradas escogiendo el metodo que mas te guste.')
print('----------------------------------------------')
print('1. Para numeracion exhaustiva\
    2. Busqueda binaria\
        3. Aproximacion')

metodo = int(input('Cual escoges: '))

if metodo == 1:
    enumeracion()
elif metodo == 2:
    busqueda_binaria()
elif metodo == 3:
    aproximacion()
else:
    print('Solo son aceptadas las opciones 1, 2 y 3')



