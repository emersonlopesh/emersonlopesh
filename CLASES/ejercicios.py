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
    

