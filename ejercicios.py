#1 Crear un programa que me pida la edad de una persona si la edad es mayor o igual a 18 que me muestre un mensaje 'eres mayor de edad caso contrario que me muestre un mensaje ''eres menor de edad '

edad = int(input("Ingresa tu edad: "))
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")


#2 Una tienda comercial desea hacer un descuento del 20%, crear un programa que me determine si el cliente se hace acreedor del descuento teniendo en cuenta los siguiente, si el cliente realiza una compra es igual o mayor a 1000 soles mostrar un mensaje que diga 'ganaste el descuento del 20% ahora pagarás< mostrar el total de la compra menos el descuento >en caso de la compra no supere los 1000 soles entonces mostrar un mensaje que diga 'no aplicas al descuento <mostrar el monto de la compra>'


monto_compra = float(input("Ingrese el monto de la compra: "))

if monto_compra >= 1000:
    descuento = monto_compra * 0.2
    total_pagar = monto_compra - descuento
    print(f"Ganaste el descuento del 20%. Ahora pagarás {total_pagar} soles.")
else:
    print(f"No aplicas al descuento. El monto de la compra es {monto_compra} soles.")
    
    #3 crear un programa que me pida 5 veces un nombre y por cada vez que lo pida muestre la cantidad de veces que ingreso el nombre


nombres = {}
contador = 0

while contador < 5:
    nombre = input("Ingresa un nombre: ")
    
    if nombre in nombres:
        nombres[nombre] += 1
    else:
        nombres[nombre] = 1
    
    contador += 1

for nombre, cantidad in nombres.items():
    print(f"El nombre {nombre} fue ingresado {cantidad} veces.")


#4 crear un programa que pida un numero y lo evalue con el numero premiado si el numero ingresado es el premiado el programa finalizara si el numero ingresado es incorrecto el programa seguira pidiendo el numero premiado



numero_premiado = 1234

for i in range(3):
    numero = int(input("Ingresa un número: "))
    
    if numero == numero_premiado:
        print("¡Felicidades! Has ingresado el número premiado.")
        break
    else:
        print("Número incorrecto. Sigue intentando.")