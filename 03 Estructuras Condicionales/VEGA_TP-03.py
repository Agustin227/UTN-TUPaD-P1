ejercicio = input("seleccione un ejercicio para ejecutar: ")

match ejercicio:
    case "1":
        # Ejercicio 1

        # Definicion de variable edad
        edad = int(input("Ingrese su edad: "))

        # Condicional if
        if edad >= 18:
            print("Es mayor de edad: ")

match ejercicio:
    case "2":
        # Ejercicio 2

        # Definicion de variable nota
        nota = int(input("Ingrese su nota: "))

        # Estructura condicional if-else
        if nota >= 6:
            print("Aprobado")
        else:
            print("Desaprobado")

match ejercicio:
    case "3":
        # Ejercicio 3

        # Definicion de variable numero
        numero = int(input("ingrese un numero: "))

        # Estructura condicional else-if
        if (numero % 2 == 0):
            print("Ha ingresado un numero par ")
        else: 
            print("Por favor, ingrese un numero par ")

match ejercicio:
    case "4":
        # Ejercicio 4

        # Definicion de variable edad
        edad = int(input("Ingrese su edad: "))

        # Condicionales if-elif-else para determinar la edad
        if edad >= 30:
            print("Adulto/a ")
        elif edad >= 18 and edad < 30:
            print("Adulto/a joven ")
        elif edad >= 12 and edad < 18:
            print("Adolecente ")
        else:
            print("Niño/a")

match ejercicio:
    case "5":
        # Ejercicio 5

        # Definicion de la variable clave, tambien se obtiene la cantidad de caracteres que contiene esta variable mediante el uso de la funcion len()
        clave = input("Escriba su contraseña: ")
        cantidad = len(clave)

        # Este condicional determina si la longitud de la contraseña es adecuada 
        if cantidad >= 8 and cantidad <= 14:
            print("Ha ingresado una contraseña correcta")
        else:
            print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

match ejercicio:
    case "6":
        # Ejercicio 6

        # Importamos las librerias
        import random
        from statistics import mode, median, mean

        # Generamos una lista con 50 numeros aleatorios entre 1 y 100
        numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

        # Calculamos los parametros estadísticos
        media = mean(numeros_aleatorios)
        mediana = median(numeros_aleatorios)
        moda = mode(numeros_aleatorios)

        # Mostramos los valores calculados
        print(f"Números: {numeros_aleatorios}")
        print(f"Media: {media}")
        print(f"Mediana: {mediana}")
        print(f"Moda: {moda}")

        # Condicionales que determinan el tipo de sesgo
        if media > mediana > moda:
            print("Sesgo positivo ")
        elif media < mediana < moda:
            print("Sesgo negativo ")
        elif media == mediana == moda:
            print("Sin sesgo ")
        else:
            print("No se puede determinar un sesgo claro.")

match ejercicio:
    case "7":
        # Ejercicio 7

        # Definimos la variable palabra y guardamos su ultima letra en la variable letra
        palabra = input("Escriba una palabra: ")
        letra = palabra[-1]

        # Si la ultima letra es caulquier vocal, se imprime con un signo de exclamacion. Sino, se imprime solo la misma palabra
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u": 
            print(f"{palabra}!")
        else:
            print(palabra)

match ejercicio:
    case "8":
        # Ejercicio 8

        print("Ingrese su nombre e ingrese 1, 2 o 3 para que se imprima todo en mayusculas, todo en minusculas o la primer letra en mayusculas")

        # En estas dos variables se guarda el nombre y la opcion que se ingresan
        nombre = input("Escriba su nombre: ")
        opcion = int(input("Elija la opcio (1, 2 o 3)"))

        # Se determina como se va a imprimir el nombre segun la opcion ingresada
        if opcion == 1:
            nombre = nombre.upper()
            print(nombre)
        elif opcion == 2:
            nombre = nombre.lower()
            print(nombre)
        elif opcion == 3:
            nombre = nombre.title()
            print(nombre)
        else:
            print("Opcion no valida ")

match ejercicio:
    case "9":
        # Ejercicio 9

        # Definicion de la variable magnitud
        magnitud = float(input("Ingrese la magnitud del terremoto: "))

        # Los siguientes condicionales determinan la clasificacion de la magnitud del terremoto segun el numero ingresado
        if magnitud < 3:
            print("Muy leve ")
        elif magnitud >= 3 and magnitud < 4:
            print("Leve ")
        elif magnitud >= 4 and magnitud < 5:
            print("Moderado ")
        elif magnitud >= 5 and magnitud < 6:
            print("Fuerte ")
        elif magnitud >= 6 and magnitud < 7:
            print("Muy fuerte ")
        else:
            print("Extremo ")

match ejercicio:
    case "10":
        # Ejercicio 10

        # Definicion de variables que guardan los datos
        hemisferio = input("Ingrese N o S para indicar en que hemisferio se encuentra: ")
        mes = int(input("Ingrese el mes en el que se encuentra: "))
        dia = int(input("Ingrese el dia en el que se encuentra: "))

        # Condicionales para el hemisferio Norte
        if hemisferio == "N":
            if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
                estacion = "Invierno"
            elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
                estacion = "Primavera"
            elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
                estacion = "Verano"
            elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
                estacion = "Otoño"
            else:
                estacion = "Fecha invalida"

        # Condicionales para el hemisferio Sur
        elif hemisferio == "S":
            if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
                estacion = "Verano"
            elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
                estacion = "Otoño"
            elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
                estacion = "Invierno"
            elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
                estacion = "Primavera"
            else:
                estacion = "Fecha invalida"

        else:
            estacion = "Hemisferio no valido"

        # Mensaje final que imprime la estacion 
        print(f"La estacion es: {estacion}")