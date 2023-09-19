# tipos de datos primitivos 
'a' # string cadena texto
'hola' # esto tambien es un string
'hola soy un string y te saludo' # cadena larga 
## OBSERVACION: todo lo que este en comillas es un string
'100'
'false'
"hola"
# un string puede estar entre comillas simples o dobles 


100 ## este es un tipo de dato numerico entero integer
2.1 ## este es un tipo de dato numerico de tipo flotante float
false ## este es un tipo de dato booleano falso 
true ## tipo de dato booleano verdadero
 
 # variables 
 # es donde almacenamos nuestros tipos de dato
 # esos datos peden mutar cambiar o modificarse
 ## como creamos una variable para para almacenar nuestros datos

 #   > *NOTA:* 
Dato: es un a imformacion exacta a comparcion de atributo es una informacion exacta
atributo: varia
dato: exacto


1. Darle unnombre significativo o relacionado al dato que estamos 
almacenando.

2. Asignarle algo(indicarle a que dato esta relaciado).-> asignacion (=).

3. Indicar el tipo de dato que se va almacenar -> Darle el dato a guardar.

> Ejemplos:

Primero el dato el dato voy a pedir la edad de Nadine:
python
edad_nadine=18

Segundo dato de nombre de Edwin:
python
nombre_alumno='edwin'

# OPERADORES:
## Operadores Aritmeticos
- Suma *(+)*

- Resta *(-)*

- Multiplicacion *()**

- Division *(/)*

### Suma
> suma= 45+12
### Resta
> resta= 45-12
### Multiplicacion
>multi= 2*5
### Division
> divi= 4/2

### *OPERACION=(45+12+23)/4*

*op=15+12+14+13/4*
 
## Operadores de uso Especial

> *suma=45+42* -> Operador suma resultado 87

> *suma='45'+12* -> Operador concatenacion resultado 4512

> *saludo='hola'+'mundo'* -> Concatenacion holamundo

> *saludo2='hola'+' '+'mundo'* -> Concatenar hola mundo

> *saludos='hola'*2* ->holahola

##DATOS ESTRUCTURALES
Son tipos de datos que estan estructurados de alguna manera.

##Lista
Pueden  almacenar distintos tipos de datos en una sola lista.
python
['nombre',10,Flase]
lista_amigos['jory','edwin','adan','chinita']

##Objetos
tambien al igual que las listas almacenan distintos tipos de datos pero con un orden. Para lamacenar datos en un objeto necesitamos especificar un indice y un valor clave  ->valor 
python
alumno={
    'nombre':'jory',
    'edad':52,
    'sexo':'todos los dias'
}

##Conbinar ambas estructuras de datos

python
alumno={
    'nombre':'jory',
    'edad':30,
    'amigos'['anthony','edwin','china'],
    'direccion':´{
        'departamento':'ayacucho',
        'provincia':'lucanas',
        'distrito':'puquio',
        'jiron':'san peter',
        'numero':152
    }
}
alumnos=[{},{},{}] 
 #controles de flujo
 ##decisiones 
###solo se ejecuta el ejecuta el codigo si cumple o si la condicion es verdadera, podemos hacer que si la condicion sea falsa se ejecute otro codigo

###sintaxis
####primero especificar el codigo que se ejecutara si cumple una condicion 
#

if <condicion> 
##el codigo que desamos ejecutar si la condicion es verdad 
print('ejecuta esto')
##aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende del if 
print('esto siempre ejecuta')

#si queremos que se ejecute un codigo en caso sea falso 
if <condicion falsa>:
    print('solo immprime si es verdad')
else:
    print('solo imprime si es falso')

### ejemplito
if 15>18:
    print('si es verdad imprime esto')
else:
    print('si es falso imprime esto')
    ############
condicion=True 
if condicion:
    print('si es verdad imprime esto')
else:
    print('si es falso imprime esto')

 ##ciclos 
 ##existen dos tipos 
 ###cuando sabemos la cantidad de veces que vamos a repetir
 #para este caso existe el for
 #sintaxis despues de la palabra reservada for debemos crear una variable que almacene el numero que iremos iterando. 
 #luego tendremos que indicar el rango a iterar a los elementos a iterar
 vocales=['a','e','i','o','u']
 for i in vocales:
 print(i)











 ###cuando no sabemos la cantidad de veces a repetir 


 # FUNCIONES 
 ## existen dos tipos 


 ### 1. propias de lenguaje
 ## que ya vienen creadas e insertadas en python y estan listas para ser usadas
 ## estructura de uso de una funcion
 ## tiene el nombre seguido de parentesis podremos pasarle datos que necesita la funcion para ejecutarse 
☺[]
 ## esta es una funcion que nos sirve para mostrar por consola datos 
 print('hola') 

 ## esta funcion nos saber la longitud de una lista o un string
#len nos devuelve un numero 
print(len([1, 5, 6, 7, 8]))

# es una funcion que se detiene a esperar que el usuario introdusca informacion 
# entre parentesis podremos escribr un mensaje que indique que accion realizara el usuario 
input('ingresa ingresa')

## MAX
Esta funcion nos muestra el numero mayor de una lista 
```python
lista=[45,12,78,3,24,50]
numero_mayor=max(lista)
print(numero_mayor)
```
## MIN
Esta funcion nos muestra el numero menor de una lista 
```python
lista=[45,12,78,9,6,12]
numero_menor=min(lista)
print(numero_menor)
```
## Funcion para convertir de un string a un numero entero
```python
numero_string='100'
print(type(numero_string))
numero_entero=int(numero_string)
int('100') # ->>   100  ->> entero
```

## Funcion  para convertir un entero a un string
```python
strig(100) #  ->>  '100'  ->>  string
```

## APPEND
 funcion de python que nos permite agregar elementos al finar de una lista.
```python
ejemplo:

# lista=[15,12,78]
# elemento=100
# lista.append(elemento)
# print(lista)
```

## POP
funcion de python que nos permite eliminar los elementos que se encuentran al final de una lista(temporalmente).
```python
ejemplo:

lista=[15,12,78]
lista.pop()
print(lista)
```
## INSERT
funcion de python que nos permite agregar elementos en cualquier posicion de mi lista para eso se le tiene que pasar dos parametros, primero indicarle el indice y segundo el dato que se va a agregar.
```python
lista_nombres=['jory','nadine','bichota']
lista_nombres.insert(1,'satan')
print(lista_nombres)
```
## Remove
funcion de python que nos permite eliminar elementos de cuaquier pocision de una lista, esta funcion recibe solo el elemento que deseamos eliminar.
```python
lista=[4,5,6,8,6,7]
lista.remove(6)
print(lista)
```
## SPLIT
funcion que nos permite dividir en una lista una cadena 
```python
cadena='hola como estan'
lista=cadena.split()
print(lista)
url='www.golle.com/id=70133573
id=url.split('=').pop()
```
# 2. FUNCIONES CREADAS
## funciones propias
## pasos para crear una funcion propia
 1. hacer uso de la palabra reservada 
 2. definir un nombre de funcion que describa que tarea va a realizar
 3. establecer los parametros que recibira la funcion entre parentesis()
 4. establecer que valor o dato va retornar mi funcion con la palabra reservada return 

 > OBSERVACION =>>tambien podemos hacer uso de la funcion print () para retornar un mensaje en nuestra funcion.
 
 #### **existen dos tipos de funciones los que no resiven ningun parametro y los que resiven parametros**
python
def saludo():
    print("hola este es un saludo")

## como hacemos uso de la funcion?
## nombre de la funcion y parentesis
## funcion con parametros:
python
def mi_print(texto):
    print(texto)

print("hola este es print de python")
mi_print("hola este es mi print creado")

def suma(a,b):
    total=a+b
    return total

    suma(45,12) ##==>>>>> 57


## ejemplo
#### para que se usa esta funcion ?
#### para mostrar el valor maximo de una lista
python
lisat=[12,4,45,78,3,1]
mi_print(max(lista))

def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_mayor:
    return numero_mayor
    mi_print(mi_max(lista))
