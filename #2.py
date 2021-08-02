
class Menu_Principal:
    def __init__(self, Titulo = " ", opciones = []):
        self.Titulo = Titulo
        self.opciones = opciones
    def menu(self):
        print(self.Titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija opcion [1..{}]: ".format(len(self.opciones)))
        return opc 

opc = " "
while opc != "5":
    menu_p = Menu_Principal("Menu Principal",["1) Calculadora","2) Operación Numeros","3) Tratamiento de Listas","4) Operaciones de  Cadenas","5) Salir"])
    opc = menu_p.menu()
    if opc == "1":
        opc_1 = " "
        while opc_1 != "10":
            menu_1 = Menu_Principal("Menu Calculadora",["1) Suma","2) Resta","3) Multiplicacion","4) Division","5) Exponente","6) Valor Absoluto","7) Circunferencia","8) Area Circulo","9) Area Cuadrado","10) Salir"])
            opc_1 = menu_1.menu()
            class Calculadora:
                def __init__(self, n_1, n_2, numero):
                    self.n_1 = n_1
                    self.n_2 = n_2
                    self.numero = numero
                def ingreso():
                    global n_1, n_2, numero, lado, radio
                    n_1 = int(float(input("Ingrese un numero o la base: ")))
                    n_2 = int(float(input("Ingrese otro valor / exponente: ")))
                def datos():
                    numero = int(input("Ingrese un valor entero: "))
                def suma():
                    print("La suma es la siguiente")
                    resp = n_1 + n_2
                    print("{} + {} = {}".format(n_1, n_2, resp))
                def resta():
                    print("La resta es la siguente")
                    resp = n_1 - n_2
                    print("{} - {} = {}".format(n_1, n_2,resp))
                def mutiplicacion():
                    print("La Multiplicacion es")
                    multi = n_1 * n_2
                    print("{} * {} = {}".format(n_1,n_2,multi))
                def división():
                    print("Division de dos numeros")
                    divi = n_1 / n_2
                    print("{} / {} = {}".format(n_1,n_2,divi))
                def exponente():
                    result = n_1 ** n_2
                    print("{} ** {} = {}".format(n_1, n_2, result))   
                def valorAbsoluto():
                    if numero >= 0: return numero
                    else: return - numero
                    print(abs(numero))        
            class Cientifica(Calculadora):
                PI = 3.1416
                def __init__(self, ingreso, PI):
                    super().__init__(ingreso, PI)
                    self.PI = PI
                def ingreso_1(self):
                    lado = int(float(input("Ingrese el valor del lado del cuadrado: ")))
                    radio = int(float(input("Ingrese el valor del radio: ")))
                def  circunferencia():
                    area = PI * radio **2
                    circunf = 2 * PI * radio
                    print("El ares es {}".format(area))
                    print("Su circunferencia es {}".format(circunf))
                def areaCirculo():
                    area = PI * (radio ** 2)
                    print("El valor del radio es {}".format(area))
                def areaCuadrado():
                    perimetro = lado * 4
                    area = lado * lado
                    print("El perimetro del cuadrado es {}".format(perimetro))
                    print("El area es {}".format(area))
                if opc_1 == "1":
                    print(ingreso())
                    print(suma())
                elif opc_1 == "2":        
                    print(ingreso())
                    print(resta())
                elif opc_1 == "3":
                    print(ingreso())
                    print(mutiplicacion())        
                elif opc_1 == "4":
                    print(ingreso())
                    print(división())
                elif opc_1 == "5":
                    print(ingreso())
                    print(exponente())
                elif opc_1 == "6":
                    print(datos())
                    print(valorAbsoluto())   
                elif opc_1 == "7":
                    print(ingreso_1())
                    print(circunferencia())   
                elif opc_1 == "8":
                    print(ingreso_1())
                    print(areaCirculo())
                elif opc_1 == "9":
                    print(ingreso_1())
                    print(areaCuadrado())
                else:
                    print("Valir Incorrecto") 
    elif opc == "2":
        opc_2 = " "
        while opc_2 != "11":
            menu_2 = Menu_Principal("1)Menu Operación Numeros",["1) Presentar los números de 1 a n","2) Sumar los números de 1 a n","3) Múltiplo de cualquier numero","4) Presentar los divisores de un numero","5) Numero Primo","6) Factorial de cualquier numero","7) Fibonacci de una serie de n números","8) Perfecto","9) Primos gemelos","10) Números amigos","11) Salir"])
            opc_2 = menu_2.menu()
            class Basico:
                def __init__(self, num_1, num_2, numero, cant, numero_a):
                    self.num_1 = num_1
                    self.num_2 = num_2
                    self.numero = numero
                    self.cant = cant
                    self.numero_a = numero_a
                def dos():
                    global cant, numero, num_1, num_2, numero_a
                    cant = int(float(input("Igrese la cantidad de numeros: ")))
                    numero_a = int(float(input("Ingrese el numero: ")))
                def uno():
                    numero = int(float(input("Ingrese un numero: ")))
                def valor():
                    num_1 = int(float(input("Ingreese un numero: ")))
                    num_2 = int(float(input("Ingrese otro numero: ")))
                
                def presentar_numeros():
                    for num in range(numero):
                        print(numero + 1, end = ",")
                def multiplo():
                    return [numero_a * i for cant in range(1, cant + 1)]
                    print("Los multiplos son: ",numero_a)
                def Divisores():
                    result = [i for i in range(1, numero + 1) if numero % i == 0]
                    return result
                def primo():
                    cont = 0
                    for i in range(1, numero + 1):
                        if numero % i == 0:
                            cont += 1
                    if cont == 2:                                
                        return True
                        print("Es primo")
                    else:
                        print("No es primo")

                def perfecto():
                    suma = 0
                    for i in range(1, numero):
                        if numero % i == 0:
                            suma += i
                    return suma == numero

            class Intermedio(Basico):
                def suma_N():
                    super.suma_N(dos)
                    suma_t = 0
                    while cant > 0:
                        suma_t = suma_t + numero
                        cant = cant - 1
                    print("La suma de ciertos numeros es:{}".format(suma_t))
               
                def factorial():
                    if numero >= 0:
                        x = 1
                        f = 1
                        while x <= numero:
                            f = f * numero
                            x += 1
                            print("El factorial de ",numero,"es: ",f) # Arreglar
                    else:
                        print("No se puede calcular el factorial")

                def fibonacci():
                    a = 0
                    b = 1
                    c = 0
                    while True:
                        numero = int(float(input("Igrese la cantidad de numeros: ")))
                        if numero > 1:
                            break
                            print("1", end = " ")
                        for i in range(0, numero):
                            c = a + b
                            print(f"{c}", end = " ")
                            a = b
                            b = c
                        print(" ")

                def primosGemelos():
                    a = 0
                    if num1 > 0  and num2 > 0 and num1 != num2:
                        if num1 > num2:
                            num1 ^= num2
                            num2 ^= num1
                            num1 ^= num2
                            for i in range (num1,num2+1):
                                creciente = 2
                                esPrimo = True
                                while esPrimo and creciente < i:
                                    if i % creciente ==0:
                                        esPrimo = False
                                    else:
                                        creciente += 1
                                if esPrimo and not a:
                                    a = i
                                elif esPrimo and a:
                                    b = i
                                    if b-a == 2:
                                        print("Los numeros {} ""y {}"" son primos gemelos".format(a,b))
                                        a = i
                        else:
                            if num1 == num2:
                                print("Los numeros son iguales")
                            else:
                                print("Los numeros no son iguales")
                        return esPrimo  
    
                def  amigos():
                    for i in range(2,num1):
                        if(num1 % i==0):
                            num2=num2+i
                    return num2
                    # amigo1,amigo2=1,1
                    # num2 = amigos(n1,n2)
                    # amigo1 = amigos(n1, amigo1)
                    # amigo2 = amigos(n2, amigo2)
                    # if((amigo1==n2)and (amigo2==n1)):
                    #     print("Los numeros {}"" y {}"" si son numeros amigos".format(n1,n2))
                    # else:
                    #     print("Los numeros {}"" y {}"" no son numeros amigos".format(n1,n2))

                if opc_2 == "1":
                    print(uno())
                    print(presentar_numeros())

                elif opc_2 == "2":
                    print(uno())
                    print(suma_N())

                elif opc_2 == "3":
                    print(dos())
                    print(multiplo()) 

                elif opc_2 == "4":
                    print(uno())
                    print(Divisores())

                elif opc_2 == "5":
                    print(uno())
                    print(primo())

                elif opc_2 == "6":
                    print(uno())
                    print(factorial())

                elif opc_2 == "7":
                    print(uno())
                    print(fibonacci()) 

                elif opc_2 == "8":
                    print(uno())
                    print(perfecto())

                elif opc_2 == "9":
                    print(valor())
                    print(primosGemelos())

                elif opc_2 == "10":
                    print(valor())
                    print(amigos())                    
                else: 
                    print("El valor ingresado es incorreto")