from os import system as limpiarPantallaWindows


class OperacionesCadenas:
    def __init__(self, cadena=''):
        self.cadena = cadena
    
    def recorrerCadena(self):
        for i in self.cadena:
            print(i)
    
    def buscarCaracter(self, buscado='!'):
        encontro_caracter = self.cadena.find(buscado)
        if encontro_caracter > 0:
            print('El caracter "{}" consta dentro de la cadena.'.format(buscado))
        else:
            print('El caracter "{}" no consta en la cadena.'.format(buscado))

    def listaPosiciones(self, caracter='a'):
        lista_posiciones = []
        for i in range(0, len(self.cadena)):
            if self.cadena[i].lower() == caracter:
                lista_posiciones.append(i+1)
        return lista_posiciones

    def listaPalabras(self):
        while True:
            if len(self.cadena)+1 > 1:
                break
            else:
                print('Ingrese una palabra válida.')
                self.cadena = input('Ingrese una palabra: ').lower().replace(' ', '')

        return list(self.cadena.split())

    def cadenaLista(self):
        print('Ingreso de elementos...')
        print('Pulsar // para salir')
        lista_a_convertir = []
        while True:
            caracter_conv = input('Ingrese uno o más caracteres: ')
            if caracter_conv.replace(' ', '') == '//':
                break
            lista_a_convertir.append(caracter_conv)
        cadena_a_convertir = ''.join(lista_a_convertir)
        print('Lista:', lista_a_convertir)
        print('Cadena:', cadena_a_convertir)
    
    def insertarDato(self, buscado, posicion):
        cadena = list(self.cadena)
        cadena.insert(posicion, buscado)
        conversion_string = ''.join(cadena)
        print('Cadena nueva:', conversion_string)
    
    def eliminarOcurrencias(self, buscado):
        print('Cadena renovada:', self.cadena.lower().replace(buscado, ''))

    def retornaValor(self, posicion):
        cadena = list(self.cadena)
        vueltas = 0
        for i in posicion:
            if vueltas > 0:
                cadena.pop((i-1)-vueltas)
            else: cadena.pop(i-1)
            vueltas += 1
        return ''.join(cadena)
    
    def concatenarCadena(self, dato):
        print('Cadena concatenada:', self.cadena + dato)


def menu():
    _cadena = ''
    opc = 0
    OPC_TOTALES = 10
    while opc != 10:
        print('Menú Operaciones de Cadenas')
        print('  1) Recorrer y presentar los datos de una cadena')
        print('  2) Buscar un carácter en una cadena')
        print('  3) Retornar una lista con la posiciones dado un carácter de la cadena')
        print('  4) Retornar una lista con todas las palabras de una cadena')
        print('  5) Retornar una cadena a partir de una lista')
        print('  6) Insertar un dato en una cadena dada lo Posición')
        print('  7) Eliminar todas las ocurrencias en una cadena')
        print('  8) Retornar cualquier valor de una cadena eliminándolo ')
        print('  9) Concatenar cadenas')
        print(' 10) Salir')
        print('-----------------------------------------------------------------------\n')

        while True:
            try:
                opc = int(input('Ingrese una opción del 1...[{}]: '.format(OPC_TOTALES)))
                if opc not in range(1, 11):
                    print('Ingrese un rango disponible.')
                else: break
            except ValueError:
                print('Ingrese un número válido.')
                
        if opc != 10:
            if opc != 5:
                _cadena = input('\nIngrese una cadena: ')
            cadena = OperacionesCadenas(_cadena)
            
            if opc == 1:
                print('')
                cadena.recorrerCadena()

            elif opc == 2:
                print('')
                while True:
                    caracter_buscar = input('Ingrese el caracter a buscar: ').lower().replace(' ', '')
                    if len(caracter_buscar) > 0 and len(caracter_buscar) < 2:
                        break
                    else:
                        print('Ingrese un caracter válido.')
                cadena.buscarCaracter(caracter_buscar)

            elif opc == 3:
                print('')
                while True:
                    caracter_listar = input('Ingrese el caracter a listar: ').lower().replace(' ', '')
                    if len(caracter_listar) > 0 and len(caracter_listar) < 2:
                        break
                    else:
                        print('Ingrese un caracter válido.')
                lista_caracteres_posicion = cadena.listaPosiciones(caracter_listar)
                print('Posiciones encontradas:\n{}'.format(lista_caracteres_posicion))

            elif opc == 4:
                print('')
                lista_palabras_posicion = cadena.listaPalabras()
                print('Posiciones encontradas:\n{}'.format(lista_palabras_posicion))

            elif opc == 5:
                print('')
                cadena.cadenaLista()

            elif opc == 6:
                print('')
                insertar_dato = input('Ingrese el dato a insertar: ')
                while True:
                    try:
                        insercion_posicion = int(input('Del número 1...[{}] ingrese la posición: '.format(len(_cadena))))
                        if insercion_posicion in range(1, len(_cadena)+1):
                            break
                        else: print('Ingrese una posición correcta.')
                    except ValueError:
                        print('Ingrese valores correctos.')
                cadena.insertarDato(insertar_dato, insercion_posicion)

            elif opc == 7:
                print('')
                ocurrencia = input('Ingrese el/los caracteres a eliminar: ').lower()
                cadena.eliminarOcurrencias(ocurrencia)

            elif opc == 8:
                print('')
                print('Ingreso de posiciones...')
                print('Pulsar // para salir')
                posiciones = set()
                while True:
                    pos = input('Del número 1...[{}] ingrese las posiciones a eliminar: '.format(len(_cadena)))
                    if pos.replace(' ', '') == '//':
                        break
                    try:
                        pos = int(pos)
                        if pos in range(1, len(_cadena)+1):
                            posiciones.add(pos)
                        else: print('Ingrese una posición correcta.')
                    except ValueError:
                        print('Ingrese valores válidos.')
                valor_nuevo = cadena.retornaValor(posiciones)
                print('Cadena nueva retornada:', valor_nuevo)

            else:
                print('')
                cadena_concatenar = input('Ingrese otra cadena: ')
                cadena.concatenarCadena(cadena_concatenar)
            
        else: print('\nSaliendo...')
    
        input('\nPresione Enter para limpiar la pantalla...')
        limpiarPantallaWindows('cls')


if __name__ == '__main__':
    limpiarPantallaWindows('cls')
    menu()
