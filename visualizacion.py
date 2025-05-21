# Librerías
"""Profe creo no tengo todo lo de la anterior clase porque me puse a solucionar el tema de subida
de archivos a github, igual puse la matriz de correlacion pero no se si me quedo
faltando algo
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from analisis import DataAnalyzer
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import csv #importante para tener el formato como el orginal


data = pd.read_csv("adult.csv")
analizar = DataAnalyzer(data)

def informacion():
    try:
        text_area.delete(1.0, tk.END)
        info = analizar.summary()
        text_area.insert(tk.END, info)
    except Exception as e:
        traceback.print_exc()
        messagebox.showerror("Error", "No se puede")

def mostrar_correlacion():
    try:
        imagen = analizar.correlation_matrix()
        imagen.show()
    except Exception as e:
        traceback.print_exc()
        messagebox.showerror("Error", "No se pudo generar la matriz de correlación.")
        
        
#Tarea

def crear_formulario_usuario():
    form = tk.Toplevel()
    form.title("Registrar nuevo usuario")

    # Diccionario para guardar las entradas
    entradas = {}

    # Campos y tipos
    campos = {
        "workclass": "entry",
        "fnlwgt": "entry",
        "education": "entry",
        "education.num": "entry",
        "marital.status": ["Never-married", "Divorced", "Married-civ-spouse", "Separated", "Widowed"],
        "occupation": "entry",
        "relationship": ["Husband", "Wife", "Not-in-family", "Unmarried", "Own-child", "Other-relative"],
        "race": ["White", "Black", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other"],
        "sex": ["Male", "Female"],
        "capital.gain": "entry",
        "capital.loss": "entry",
        "hours.per.week": "entry",
        "native.country": "entry",
        "income": ["<=50K", ">50K"]
    }

    #Función para guardar los datos
    def guardar_usuario():
        nuevo_usuario = {}
        for campo, widget in entradas.items():
            valor = widget.get()
            nuevo_usuario[campo] = valor
            
        #agrega al CSV
        with open("adult.csv", "a", newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(nuevo_usuario.values())

        messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        form.destroy()

    #widgets dinamicos
    fila = 0
    for campo, tipo in campos.items():
        tk.Label(form, text=campo).grid(row=fila, column=0, sticky='e')
        if isinstance(tipo, list):
            var = tk.StringVar()
            var.set(tipo[0])
            entradas[campo] = var
            menu = tk.OptionMenu(form, var, *tipo)
            menu.grid(row=fila, column=1)
        else:
            entrada = tk.Entry(form)
            entrada.grid(row=fila, column=1)
            entradas[campo] = entrada
        fila += 1

    #boton guardar
    tk.Button(form, text="Guardar", command=guardar_usuario).grid(row=fila, columnspan=2, pady=10)
    




#aqui creo la ventana
ventana = tk.Tk()
ventana.title("Análisis de datos")

#luego los widgets que la usan
boton_summary = tk.Button(ventana, text="Info", command=informacion)
boton_summary.pack()

boton_corr = tk.Button(ventana, text="Matriz de correlación", command=mostrar_correlacion)
boton_corr.pack()

text_area = ScrolledText(ventana, width=70, height=30)
text_area.pack()

boton_formulario = tk.Button(ventana, text="Registrar nuevo usuario", command=crear_formulario_usuario)
boton_formulario.pack()


ventana.mainloop()


