from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

colorVerde = "#8ed492"
colorVerde2 = "#3f8b49"
colorRojo = "#c33333"
colorRojo2= "#990808"
colorNegro = "gray22"
colorNegro2= "gray10"
letraNegra="black"
letraBlanca="white"
colorCeleste="#405C6D"
colorGris = "#4B4B4B"
fontEntry = ("Calibri",14)

######Hacer la conexion a la base######


#######################################

#Modifique para un poquito mas alto
def centrar_ventana(anchoVentana,largoVentana):
	ancho = ventana.winfo_screenwidth()
	largo = ventana.winfo_screenheight()
	x = (ancho // 2) - (anchoVentana//2) 
	y = (largo //2) - (largoVentana//2) - 50
	ventana.geometry(f"{anchoVentana}x{largoVentana}+{x}+{y}")
def misEstilos(colorFondo,colorFondo2,colorBoton,colorLetra):
	estilos = ttk.Style()
	estilos.theme_use("alt")
	estilos.configure("titulos.TLabel",
				       background=colorFondo,
				       font = ("Calibri",20),
				       foreground= colorLetra,
				       relief=FLAT
					 )
	estilos.configure("entrada.TLabel",
				       background=colorFondo,
				       font = ("Calibri",14),
				       foreground= colorLetra,
				       relief=FLAT
					 )
	estilos.configure("botones.TFrame",
				       background=colorFondo
					 )
	estilos.configure("contenido.TFrame",
				       background=colorFondo
					 )


	estilos.configure("boton.TButton",
				       background=colorBoton,
				       foreground=colorLetra,
				       font=("Calibri",15),
				       relief=FLAT
					 )
	estilos.map("boton.TButton",
                       background = [("pressed",colorBoton),("active",colorBoton)]
					 )
	estilos.configure("botonPresionado.TButton",
				       background=colorCeleste,
				       foreground=colorLetra,
				       font=("Calibri",15),
				       relief=FLAT
					 )
	estilos.map("botonPresionado.TButton",
                       background = [("pressed",colorCeleste),("active",colorCeleste)]
					 )

	#Cambiar el cuerpo
	estilos.configure("tablaBuscar.Treeview", 
					   highlightthickness=0,
					   bd=0,
					   font=('Calibri', 11)
					 ) 
	#Cambiar encabezado
	estilos.configure("tablaBuscar.Treeview.Heading", 
					   background = colorCeleste,
					   foreground = colorLetra,
					   font=('Calibri', 13,'bold')
					 )
	estilos.map("tablaBuscar.Treeview.Heading", 
			     background = [("pressed","darkslateblue"),("active","darkslateblue")]
			   )
	#Remover bordes
	estilos.layout("tablaBuscar.Treeview", 
		            [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]
		          )
def principal():
	ventana.config(bg=colorNegro)
	misEstilos(colorNegro,colorNegro2,colorNegro2,letraBlanca)
	#ventana.state("zoomed")
	centrar_ventana(1000,600)
	ventana.title("PRINCIPAL")
	ventana.minsize(1000,600)
	frameBotones = ttk.Frame(style="botones.TFrame")
	frameBotones.pack(fill=X)
	frameContenido = ttk.Frame(style="contenido.TFrame")
	frameContenido.pack(fill=BOTH,expand=1)

	frameArticulos = ttk.Frame(frameContenido,style="contenido.TFrame")
	frameArticulos.pack(fill=BOTH,expand=1)

	labelTituloConfiguracion = ttk.Label(frameArticulos,text="Búsqueda",style="titulos.TLabel")
	labelTituloConfiguracion.pack()

	labelBuscadorArticulos = ttk.Label(frameArticulos,text="Búsqueda de articulos",style="entrada.TLabel")
	labelBuscadorArticulos.pack(fill=X,padx=80,pady=(20,0),anchor=W)
	buscadorArticulos = ttk.Entry(frameArticulos,font=("Calibri",14))
	buscadorArticulos.pack(fill=X,padx=80,pady=(0,20))
	

	tablaArticulos = ttk.Treeview(frameArticulos,style="tablaBuscar.Treeview")
	tablaArticulos["columns"] = ("marca","modelo")
	tablaArticulos.column("#0", minwidth=0,width=100,stretch=False , anchor=CENTER)
	#POdemos cambiarle el color segun tag
	tablaArticulos.tag_configure('odd', background='#D8D7D7')
	tablaArticulos.tag_configure('even', background='snow')
	#heading = encabezado
	tablaArticulos.heading("#0",text="Código")
	tablaArticulos.heading("marca",text="Marca")
	tablaArticulos.heading("modelo",text="Modelo")
	tablaArticulos.pack(pady=10,padx=80,fill=BOTH,ipady=100)

	##Esto lo borran cuando agreguen buscar en la base##
	datosBuscados = [
			(1,"Ford","Duster"),
			(2,"Ford","F100"),
			(3,"Renault","Duster"),
			(4,"Renault","Clio")
		]
	####################---------#######################

	def buscarArticulos(evento):
		### Aca se buscaria en la base de datos
		### en datos buscados estarian nuestros datos

		#Borrar tabla
		for fila in tablaArticulos.get_children():
			tablaArticulos.delete(fila)
		#Insertar datos en treeview
		for dato in datosBuscados:
			tablaArticulos.insert("",END,text=dato[0],values=(dato[1],dato[2]))
	buscadorArticulos.bind("<Key>",buscarArticulos)
def run():
	global ventana
	ventana = Tk()
	principal()
	ventana.mainloop()

run()

