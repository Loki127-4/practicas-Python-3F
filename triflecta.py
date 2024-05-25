#al iniciar se nos debe pedir ingresar un numero, si este es mayor a 0 el programa inicia, de lo contrario finaliza (tambien si se ingresa otra cosa que no sea un numero). 
#Se debe poder ingresar una palabra o frase y contar cuantos caracteres tiene dicha palabra  o frase. 
#Con el valor obtenido en el punto anterior calcular su factorial, una ve hecho esto, decirnos si el resulto es par o impar. 
#Se deben imprimir los resultados por pantalla en cada paso. 
#Una vez cumplido esto, deberemos volver a pedir el ingreso de un numero y realizar la verificacion del punto 1

condicion=True

while condicion:
    numero_ingresado=int(input("ingrese un número mayor a cero : "))

    if numero_ingresado > 0:
        palabra_frase=input("Ingrese una palabra o frase : ")
        longitud=len(palabra_frase)
        print(f"La longitud de la palabra/frase ingresada es de:{longitud} ")
        if longitud%2==0:
            print("El factorial es par")
        else:
            print("El factorial es impar")
    else:
        print("No se puede comenzar")
        break
    
    

