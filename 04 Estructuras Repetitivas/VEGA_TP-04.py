
ejercicio = int(input("Seleccione un ejercicio (del 1 al 10) para ejecutar: "))


match ejercicio:
        case 1:
            # Ejercicio 1

            for i in range(101):
                print(i)

        case 2:
            # Ejercicio 2

            numero = int(input("Ingrese un numero entero: "))
            numero = abs(numero)

            # Si el numero es 0, lo tratamos como un digito
            if numero == 0:
                print("El numero tiene 1 dígito.")
            else:
                contador = 0
                while numero > 0:
                    numero = numero // 10
                    contador += 1
                print(f"El numero tiene {contador} digitos.")

        case 3:
            #cEjercicio 3

            # Ingresar los dos valores
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))

            # Determinar el menor y el mayor
            inicio = min(a, b) + 1
            fin = max(a, b)

            # Inicializar suma en 0
            suma = 0

            # Sumar los numeros entre ellos 
            for i in range(inicio, fin):
                suma += i

            # Mensaje final
            print(f"La suma de los números entre {a} y {b} es: {suma}")

        case 4:
            # Ejercicio 4

            # Inicializar la suma en 0
            suma = 0

            # Ciclo while
            while True:
                numero = int(input("Ingrese un numero o ingrese un 0 para salir: "))
                
                if numero == 0:
                    break

                suma += numero

            # Mensaje final
            print(f"La suma total de los numeros ingresados es: {suma}")

        case 5:
            # Ejercicio 5

            import random

            # Generar numero aleatorio
            numero = random.randint(0, 9)

            # Inicio de variable de intentos en 0 y variable booleana en falso
            intentos = 0
            adivinado = False


            # Ciclo while
            while not adivinado:
                intento = int(input("Adivina el numero entre 0 y 9: "))
                intentos += 1

                if intento == numero:
                    adivinado = True
                    print(f"Muy bien. Adivinaste el numero en {intentos} intentos.")
                else:
                    print("Incorrecto, intenta de nuevo.")

        case 6:
            # Ejercicio 6

            # Ciclo for que decrece desde 100 hasta 0 de 2 en 2
            for i in range(100, -1, -2):
                print(i)

        case 7:
            # Ejercicio 7

            # Se pide ingresar un numero positivo
            n = int(input("Ingrese un numero entero positivo: "))

            # Ciclo while que lo valida
            while n < 0:
                print("Numero invalido. Debe ser positivo.")
                n = int(input("Ingrese un número entero positivo: "))

            # Inicio de la suma en 0 y ciclo for que realiza las sumas
            suma = 0
            for i in range(n + 1):
                suma += i

            # Mensaje final
            print(f"La suma de los numeros del 0 al {n} es: {suma}")

        case 8:
            # Ejercicio 8

            # Inicio de todas las variables en 0
            pares = 0
            impares = 0
            positivos = 0
            negativos = 0

            # Ciclo for para contar
            for i in range(100):
                numero = int(input(f"Ingrese el numero {i + 1}: "))
                
                # Par o impar
                if numero % 2 == 0:
                    pares += 1
                else:
                    impares += 1
                
                # Positivo o negativo
                if numero > 0:
                    positivos += 1
                elif numero < 0:
                    negativos += 1

            # Mostrar resultados
            print(f"Pares: {pares}")
            print(f"Impares: {impares}")
            print(f"Positivos: {positivos}")
            print(f"Negativos: {negativos}")

        case 9:
            # Ejercicio 9

            # Inicio la suma en 0
            suma = 0

            # Ciclo for para sumar
            for i in range(100):
                numero = int(input(f"Ingrese el numero {i + 1}: "))
                suma += numero

            # Calculo de la media
            media = suma / 100
            print(f"La media de los 100 números ingresados es: {media}")

        case 10:
            # Ejercicio 10

            # Definicion de variables
            numero = int(input("Ingrese un numero: "))
            numero_original = abs(numero)  
            numero_invertido = 0

            # Ciclo whilw
            while numero_original > 0:
                digito = numero_original % 10         
                numero_invertido = numero_invertido * 10 + digito
                numero_original = numero_original // 10  

            # Si el número original era negativo, se conserva el signo
            if numero < 0:
                numero_invertido = -numero_invertido

            print(f"Numero invertido: {numero_invertido}")

