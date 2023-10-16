#importamos tkinter
from tkinter import *
#instanciar la clase Tk()
ventana=Tk()
ventana.geometry("400x500")
#creo mid dos widget de orden con la clase Flame()
widget_uno=Frame()
widget_uno.grid(row=0,column=0)
widget_uno.config(width=400,height=50)

#creacion de etiquetas
etiqueta=Label(ventana,text="ingressa su nombre")
etiqueta.grid(row=1,column=0)


#creacion de cuadros de texto
cuadro_texto=Entry()
cuadro_texto.grid(row=2,column=0)

#usar el metodo loop para que la ventana permanesca abierta
ventana.mainloop()




from tkinter import *
ventana = Tk()

etiqueta_nombre = Label(ventana, text='Nombre y apellido:')
etiqueta_nombre.grid(row=0, column=0)

cuadro_nombre_y_apellido = Entry(ventana)
cuadro_nombre_y_apellido.grid(row=0, column=1)




etiqueta_dni = Label(ventana, text='DNI:')
etiqueta_dni.grid(row=2, column=0)

cuadro_dni = Entry(ventana)
cuadro_dni.grid(row=2, column=1)


etiqueta_celular = Label(ventana, text='Celular:')
etiqueta_celular.grid(row=3, column=0)

cuadro_celular = Entry(ventana)
cuadro_celular.grid(row=3, column=1)


ventana.geometry('380x500')

cuadro_rojo = Frame(ventana, bg='green', width=200, height=120)
cuadro_rojo.grid(row=6, column=0, columnspan=2)

ventana.mainloop()