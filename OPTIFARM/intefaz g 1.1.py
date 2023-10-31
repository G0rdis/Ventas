import tkinter as tk
from tkinter import ttk, Entry, Label, Button, StringVar, OptionMenu
from PIL import Image, ImageTk
from tkinter import filedialog
# Diccionario de producción y precios
produccion = {
    "Naranjas": 10000,
    "Mandarinas": 7000,
    "Limones": 4000,
    "Mangos": 6000
}

precios = {
    "Naranjas": {
        "Mayorista": 1500,
        "Venta al por menor": 2000
    },
    "Mandarinas": {
        "Mayorista": 1800,
        "Venta al por menor": 2200
    },
    "Limones": {
        "Mayorista": 2000,
        "Venta al por menor": 2500
    },
    "Mangos": {
        "Mayorista": 2200,
        "Venta al por menor": 2800
    }
}

# Diccionario para almacenar pedidos de los consumidores
pedidos = {}

# Función para calcular ingresos
def calcular_ingresos(pedido):
    ingresos_totales = 0
    for producto, cantidades in pedido.items():
        for canal, cantidad in cantidades.items():
            precio = precios[producto][canal]
            ingresos_totales += precio * cantidad
    return ingresos_totales

# Función para registrar un pedido
def registrar_pedido():
    def registrar():
        nombre_consumidor = entrada_nombre_consumidor.get()
        producto = entrada_producto.get()
        cantidad = float(entrada_cantidad.get())
        canal = canal_var.get()
        if nombre_consumidor not in pedidos:
            pedidos[nombre_consumidor] = {}
        if producto not in pedidos[nombre_consumidor]:
            pedidos[nombre_consumidor][producto] = {}
        pedidos[nombre_consumidor][producto][canal] = cantidad
        ventana_pedido.destroy()

    # Ventana para registrar un pedido
    ventana_pedido = tk.Toplevel()
    ventana_pedido.title("REGISTRAR PEDIDO")
    ventana_pedido.geometry("600x600")

    # Configuración de etiquetas en verde con fuente Arial 14
    label_nombre_consumidor = Label(ventana_pedido, text="Nombre del consumidor:", bg="green", fg="white", font=("Arial", 14))
    label_producto = Label(ventana_pedido, text="Producto a comprar:", bg="green", fg="white", font=("Arial", 14))
    label_cantidad = Label(ventana_pedido, text="Cantidad en kg:", bg="green", fg="white", font=("Arial", 14))
    label_canal_distribucion = Label(ventana_pedido, text="Canal de distribución:", bg="green", fg="white", font=("Arial", 14))

    # Resto de las etiquetas y configuración de entrada aquí...
    entrada_nombre_consumidor = Entry(ventana_pedido, font=("Arial", 14))
    entrada_producto = Entry(ventana_pedido, font=("Arial", 14))
    entrada_cantidad = Entry(ventana_pedido, font=("Arial", 14))
    canal_var = StringVar()
    canal_option = OptionMenu(ventana_pedido, canal_var, "Mayorista", "Venta al por menor")

    # Botón para registrar el pedido
    boton_registrar = Button(ventana_pedido, text="Registrar Pedido", command=registrar,
                            font=("Arial", 14), bg="green", fg="white")

    # Posición de los elementos
    label_nombre_consumidor.grid(row=0, column=0, padx=10, pady=10)
    entrada_nombre_consumidor.grid(row=0, column=1, padx=10, pady=10)
    label_producto.grid(row=1, column=0, padx=10, pady=10)
    entrada_producto.grid(row=1, column=1, padx=10, pady=10)
    label_cantidad.grid(row=2, column=0, padx=10, pady=10)
    entrada_cantidad.grid(row=2, column=1, padx=10, pady=10)
    label_canal_distribucion.grid(row=3, column=0, padx=10, pady=10)
    canal_option.grid(row=3, column=1, padx=10, pady=10)
    boton_registrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
# Función para cargar la imagen de fondo
# Función para cargar una imagen de fondo desde un archivo seleccionado por el usuario
def cargar_imagen_de_fondo(ventana):
    # Solicitar al usuario que seleccione un archivo de imagen
    ruta_imagen = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.gif")])
    
    if ruta_imagen:
        img = Image.open(ruta_imagen)
        img = ImageTk.PhotoImage(img)
        
        etiqueta_imagen = tk.Label(ventana, image=img)
        etiqueta_imagen.place(x=0, y=0, relwidth=1, relheight=1)

        ventana.img = img

# Función principal
def main():
    ventana = tk.Tk()
    ventana.title("Sistema de Pedidos")

    # Botón para cargar la imagen de fondo
    boton_cargar_imagen = tk.Button(ventana, text="Cargar Imagen de Fondo", command=lambda: cargar_imagen_de_fondo(ventana))
    boton_cargar_imagen.pack()

    ventana.geometry("1280x720")  # Ajusta las dimensiones según el tamaño de tu ventana

    ventana.mainloop()

if __name__ == "__main__":
    main()