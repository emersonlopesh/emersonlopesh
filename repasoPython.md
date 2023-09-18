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

## DATOS ESTRUCTURALES
Son tipos de datos que estan estructurados de alguna manera.

## Lista
Pueden  almacenar distintos tipos de datos en una sola lista.
python
['nombre',10,Flase]
lista_amigos['jory','edwin','adan','chinita']

## Objetos
tambien al igual que las listas almacenan distintos tipos de datos pero con un orden. Para lamacenar datos en un objeto necesitamos especificar un indice y un valor clave  ->valor 
python
alumno={
    'nombre':'jory',
    'edad':52,
    'sexo':'todos los dias'
}

## Conbinar ambas estructuras de datos

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
 # controles de flujo
 ## decisiones 
### solo se ejecuta el ejecuta el codigo si cumple o si la condicion es verdadera, podemos hacer que si la condicion sea falsa se ejecute otro codigo

### sintaxis
#### primero especificar el codigo que se ejecutara si cumple una condicion 
#

if <condicion> 
## el codigo que desamos ejecutar si la condicion es verdad 
print('ejecuta esto')
## aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende del if 
print('esto siempre ejecuta')

# si queremos que se ejecute un codigo en caso sea falso 
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

 ## ciclos 