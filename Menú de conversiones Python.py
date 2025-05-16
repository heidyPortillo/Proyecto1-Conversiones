import tkinter as tk    
from tkinter import messagebox
from tkinter import ttk 
from tkinter import font

def metros_kilometros(x):return x/1000
def pulgadas_metros(x): return x*0.0254
def kilogramos_gramos(x): return x *1000
def libras_kilogramos(x): return x*0.45
def segundos_minutos(x): return x /60
def horas_dias(x): return x /24

def realizar_conversion(entry, label_resultado, funcion):
    try:
        valor=float(entry.get())
        resultado = funcion(valor)
        label_resultado.config(text=f"Resultado: {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor válido")


def abrir_ventana_conversion(opción):
    win = tk.Toplevel()
    win.title(f"Conversión de {opción}")
    win.geometry("350x250")
    win.configure(bg="#E6E6FA")
    costume_font = ("Segoe UI", 10, "italic")

    if opción == "Longitud":
        opciones = [("Metros a Kilómetros", metros_kilometros), ("Pulgadas a metros", pulgadas_metros)]
    elif opción == "Masa":
        opciones= [("Kilogramos a gramos", kilogramos_gramos), ("Libras a kilogramos", libras_kilogramos)]
    elif opción == "Tiempo":
        opciones = [("Segundos a minutos", segundos_minutos), ("Horas a días", horas_dias)]
    else:
        return

    for texto, funcion in opciones:
        tk.Label(win, text=texto, font=costume_font, bg="#E6E6FA").pack(pady=5)
        entry = tk.Entry(win)
        entry.pack()
        resultado = tk.Label(win, text="Resultado:", font=costume_font, bg="#E6E6FA")
        resultado.pack()
        boton = tk.Button(win, text="Convertir",
                            command=lambda e=entry, l=resultado, bg="#E6E6FA", font=costume_font, f=funcion: realizar_conversion(e, l, f))
        boton.pack(pady=10)

def mostrar_selector():
    ventana = tk.Tk()
    ventana.title("Factores de conversión")
    ventana.geometry("300x200")
    ventana.configure(bg="#E6E6FA")
    costume_font = ("Segoe UI", 10, "italic")

    tk.Label(ventana, text="Selecciona un tipo de conversión", font=costume_font, bg="#E6E6FA").pack(pady=10)


    factores=["Longitud", "Masa", "Tiempo"]

    combo = ttk.Combobox(ventana, values=factores, font=costume_font)
    combo.pack(pady=10)

    def abrir():
        seleccion = combo.get()
        if seleccion:
            abrir_ventana_conversion(opción=seleccion)
        else:
            messagebox.showwarning("Cuidado", "Seleccione una opción")

    tk.Button(ventana, text="Aceptar", command=abrir, font=costume_font).pack(pady=20)
    ventana.mainloop()

mostrar_selector()


