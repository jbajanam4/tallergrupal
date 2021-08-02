class Lista(Intermedio):
    def _init_(self, lista=[], num=0):
        self.lista = lista
        self.num = num

    def presentar_lista(self):
        print('Recorriendo una lista')
        if len(self.lista) != 0:
            for elemento in range(len(self.lista)):
                if elemento+1 != len(self.lista): print(self.lista[elemento] + ', ', end='')
                else: print(self.lista[elemento] + '.')
        else: print('No hay elemento que recorrer.')

    def buscar_lista(self, valor=''):
        print('Buscar un valor')
        if len(self.lista) != 0:
            ubicacion_del_valor = []
            for posicion, elemento in enumerate(self.lista):
                if elemento == valor: ubicacion_del_valor.append(posicion+1)
            if not not ubicacion_del_valor:  # Entrar solo si hay elementos en lista ubicacion_del_valor.
                print('El valor', valor, 'se encontró en la posición: ', end='')
                for elemento in range(len(ubicacion_del_valor)):  # Recorrer lista ubicacion_del_valor.
                    if elemento+1 != len(ubicacion_del_valor): print(str(ubicacion_del_valor[elemento]) + ', ', end='')
                    else: print(str(ubicacion_del_valor[elemento]) + '.')
            if not ubicacion_del_valor: print('El valor', valor, 'no se encontró en la lista.')
        else: print('No hay valor que buscar porque la lista está vacía.')

    def lista_factorial(self):
        lista_factorial = []
        print('Lista con ', end='')
        Intermedio.factorial(self, self.num)
        for numero_inver in reversed(range(1, self.num+1)):  # reversed revierte el rango de numero.
            lista_factorial.append(numero_inver)
        return lista_factorial

    def primo(self):
        lista_primo = []
        primo = False
        print('Lista de números primos hasta el', self.num)
        for numero in range(self.num+1):
            if numero >= 2:
                for numero_indiv in range(2, numero):
                    if numero % numero_indiv == 0:
                        primo = True
                        break
                if not primo: lista_primo.append(numero)
            else: pass
            primo = False
        return lista_primo

    def lista_notas(self, lista_notas_dict={}):
        print('Lista con notas de alumnos')
        for alumno in lista_notas_dict:
            print(alumno, 'estas son tus notas -> ', end='')
            print('| ', end='')
            for nota in lista_notas_dict[alumno]:
                print(nota, end=' | ')
            print('')

    def insertar_lista(self, posicion=0, valor=0):
        print('Insertar valor en lista según su posición')
        print('Lista antigua ->', self.lista)
        self.lista.insert(posicion-1, valor)
        print('Lista nueva   ->', self.lista)

    def eliminar_lista(self, valor=''):
        print('Eliminar todas las ocurrencias de una lista')
        elementos_repetidos = self.lista.count(valor)
        print('Lista antigua ->', self.lista)
        if elementos_repetidos:
            for _ in range(elementos_repetidos):
                self.lista.remove(valor)
            print('Lista nueva   ->', self.lista)
        else: print('No se encontro ese elemento.')

    def retornar_valor_lista(self, posicion=0):
        print('Retorna cualquier valor de una lista eliminandolo')
        try:
            return self.lista[posicion-1]
        except IndexError:
            print('No existen los suficientes elementos para poder eliminar esa posición de la lista.')
            print('Ingrese otra posición.')

    def copiar_tupla_lista(self, tupla=('Tupla', 'convertida', 'en', 'List@.')):
        print('Copiar tupla a lista\nTupla ya creada...')
        print('Tupla ->', tupla)
        print('Lista ->', list(tupla))

    def vuelto_lista(self, lista_clientes_diccionario={}):
        print('Dar el vuelto a varios clientes')
        for vuelto in lista_clientes_diccionario:
            print('$' + str(vuelto) + ' será entregado a los siguientes clientes -> ', end='')
            print('- ', end='')
            for cliente in lista_clientes_diccionario[vuelto]:
                print(cliente + ' - ', end='')
            print('')