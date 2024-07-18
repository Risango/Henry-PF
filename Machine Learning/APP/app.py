import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
import json
import pandas as pd
import os
import sys

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

csv_file_path = resource_path("Business_ModeloRecomendacion.csv")
dfBusiness = pd.read_csv(csv_file_path)
dfBusiness = dfBusiness[dfBusiness["name"] == "Dunkin'"]
dfBusiness = dfBusiness[["business_id", "name"]]

# Colores
BG_COLOR = "#3a3a3a"  # Gris oscuro
FG_COLOR = "#f5b700"  # Amarillo oscuro
TEXT_COLOR = "#ffffff"  # Blanco

def configurar_colores(widget):
    widget.configure(bg=BG_COLOR, fg=TEXT_COLOR)
    if isinstance(widget, tk.Text):
        widget.configure(background="#505050", foreground=TEXT_COLOR, insertbackground=TEXT_COLOR)
    elif isinstance(widget, tk.Entry):
        widget.configure(background="#505050", foreground=TEXT_COLOR, insertbackground=TEXT_COLOR)

def aplicar_estilos():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", background=BG_COLOR, foreground=TEXT_COLOR)
    style.configure("TButton", background=BG_COLOR, foreground=TEXT_COLOR)
    style.configure("TCombobox", fieldbackground=BG_COLOR, background=BG_COLOR, foreground=TEXT_COLOR)
    style.map("TButton", background=[("active", BG_COLOR)], foreground=[("active", TEXT_COLOR)])
    style.map("TCombobox", background=[("readonly", BG_COLOR)], fieldbackground=[("readonly", BG_COLOR)], foreground=[("readonly", TEXT_COLOR)])

def mostrar_recomendaciones():
    global business_id_var, name_var, business_id_combobox, name_combobox, negocio_text, usuarios_text

    recomendador_window = tk.Toplevel(root)
    recomendador_window.title("Business ID Recommender")
    recomendador_window.configure(bg=BG_COLOR)

    label = ttk.Label(recomendador_window, text="Seleccione Business ID o Nombre:")
    label.pack(pady=5)

    business_id_var = tk.StringVar()
    name_var = tk.StringVar()

    business_id_combobox = ttk.Combobox(recomendador_window, textvariable=business_id_var, values=dfBusiness["business_id"].tolist())
    business_id_combobox.pack(pady=5)
    business_id_combobox.bind("<<ComboboxSelected>>", actualizar_name_combobox)

    name_combobox = ttk.Combobox(recomendador_window, textvariable=name_var, values=dfBusiness["name"].tolist())
    name_combobox.pack(pady=5)
    name_combobox.bind("<<ComboboxSelected>>", actualizar_business_id_combobox)

    button = ttk.Button(recomendador_window, text="Enviar", command=enviar_request)
    button.pack(pady=5)

    negocio_label = ttk.Label(recomendador_window, text="Información del Negocio:")
    negocio_label.pack(pady=5)
    negocio_text = tk.Text(recomendador_window, height=10, width=80)
    negocio_text.pack(pady=5)
    configurar_colores(negocio_text)

    usuarios_label = ttk.Label(recomendador_window, text="Usuarios Recomendados:")
    usuarios_label.pack(pady=5)
    usuarios_text = tk.Text(recomendador_window, height=20, width=80)
    usuarios_text.pack(pady=5)
    configurar_colores(usuarios_text)

def actualizar_name_combobox(event):
    selected_business_id = business_id_var.get()
    name = dfBusiness.loc[dfBusiness["business_id"] == selected_business_id, "name"].values[0]
    name_var.set(name)

def actualizar_business_id_combobox(event):
    selected_name = name_var.get()
    business_id = dfBusiness.loc[dfBusiness["name"] == selected_name, "business_id"].values[0]
    business_id_var.set(business_id)

def enviar_request():
    business_id = business_id_var.get()
    if not business_id:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un Business ID")
        return

    url = "https://recomendacionusuarios-3bgweof3mq-uc.a.run.app"
    try:
        response = requests.post(url, json={'business_id': business_id})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo completar la solicitud: {e}")
        return

    try:
        json_response = response.json()
        
        # Eliminar duplicados en "usuarios_recomendados"
        if "usuarios_recomendados" in json_response:
            usuarios_recomendados = json_response["usuarios_recomendados"]
            usuarios_unicos = {usuario["User_id"]: usuario for usuario in usuarios_recomendados}
            json_response["usuarios_recomendados"] = list(usuarios_unicos.values())
        
        # Mostrar información del negocio
        negocio_info = json_response.get("negocio_info", {})
        negocio_info_text = json.dumps(negocio_info, indent=4, ensure_ascii=False)
        negocio_text.delete(1.0, tk.END)
        negocio_text.insert(tk.END, negocio_info_text)

        # Mostrar usuarios recomendados
        usuarios_recomendados = json_response.get("usuarios_recomendados", [])
        usuarios_recomendados_text = json.dumps(usuarios_recomendados, indent=4, ensure_ascii=False)
        usuarios_text.delete(1.0, tk.END)
        usuarios_text.insert(tk.END, usuarios_recomendados_text)
    except json.JSONDecodeError:
        messagebox.showerror("Error", "No se pudo decodificar la respuesta como JSON")
        negocio_text.delete(1.0, tk.END)
        usuarios_text.delete(1.0, tk.END)

def mostrar_prediccion_exito():
    global stars_entry, review_count_entry, state_combobox, prediccion_text

    prediccion_window = tk.Toplevel(root)
    prediccion_window.title("Predicción de Éxito")
    prediccion_window.configure(bg=BG_COLOR)

    stars_label = ttk.Label(prediccion_window, text="Ingrese Stars (0-5):")
    stars_label.pack(pady=5)

    stars_entry = tk.Entry(prediccion_window, width=50, validate="key", validatecommand=(root.register(validar_stars), '%P'))
    stars_entry.pack(pady=5)
    configurar_colores(stars_entry)

    review_count_label = ttk.Label(prediccion_window, text="Ingrese Review Count:")
    review_count_label.pack(pady=5)

    review_count_entry = tk.Entry(prediccion_window, width=50, validate="key", validatecommand=(root.register(validar_review_count), '%P'))
    review_count_entry.pack(pady=5)
    configurar_colores(review_count_entry)

    state_label = ttk.Label(prediccion_window, text="Seleccione State:")
    state_label.pack(pady=5)

    state_combobox = ttk.Combobox(prediccion_window, values=["PA", "FL", "MO", "TN", "IN"], width=47)
    state_combobox.pack(pady=5)

    button = ttk.Button(prediccion_window, text="Enviar", command=enviar_prediccion_request)
    button.pack(pady=5)

    prediccion_label = ttk.Label(prediccion_window, text="Pocicionamiento del negocio:")
    prediccion_label.pack(pady=5)
    prediccion_text = tk.Text(prediccion_window, height=10, width=80)
    prediccion_text.pack(pady=5)
    configurar_colores(prediccion_text)

def validar_stars(value_if_allowed):
    """Valida que el valor ingresado en el campo de 'stars' esté entre 0 y 5."""
    if value_if_allowed:
        try:
            value = float(value_if_allowed)
            if 0 <= value <= 5:
                return True
            else:
                return False
        except ValueError:
            return False
    return True

def validar_review_count(value_if_allowed):
    """Valida que el valor ingresado en el campo de 'review_count' sea un entero positivo."""
    if value_if_allowed:
        return value_if_allowed.isdigit() and int(value_if_allowed) > 0
    return True

def enviar_prediccion_request():
    stars = stars_entry.get()
    review_count = review_count_entry.get()
    state = state_combobox.get()

    if not stars or not review_count or not state:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")
        return

    url = "https://prediccionexito-3bgweof3mq-uc.a.run.app"
    try:
        response = requests.post(url, json={'stars': stars, 'review_count': review_count, 'state': state})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo completar la solicitud: {e}")
        return

    try:
        json_response = response.json()
        prediccion_text.delete(1.0, tk.END)
        prediccion_text.insert(tk.END, json.dumps(json_response, indent=4, ensure_ascii=False))
    except json.JSONDecodeError:
        messagebox.showerror("Error", "No se pudo decodificar la respuesta como JSON")
        prediccion_text.delete(1.0, tk.END)

def opcion3():
    global business_id_var_3, name_var_3, business_id_combobox_3, name_combobox_3, estados_text

    opcion3_window = tk.Toplevel(root)
    opcion3_window.title("Recomendación de Estados")
    opcion3_window.configure(bg=BG_COLOR)

    label = ttk.Label(opcion3_window, text="Seleccione Business ID o Nombre:")
    label.pack(pady=5)

    business_id_var_3 = tk.StringVar()
    name_var_3 = tk.StringVar()

    business_id_combobox_3 = ttk.Combobox(opcion3_window, textvariable=business_id_var_3, values=dfBusiness["business_id"].tolist())
    business_id_combobox_3.pack(pady=5)
    business_id_combobox_3.bind("<<ComboboxSelected>>", actualizar_name_combobox_3)

    name_combobox_3 = ttk.Combobox(opcion3_window, textvariable=name_var_3, values=dfBusiness["name"].tolist())
    name_combobox_3.pack(pady=5)
    name_combobox_3.bind("<<ComboboxSelected>>", actualizar_business_id_combobox_3)

    button = ttk.Button(opcion3_window, text="Enviar", command=enviar_request_3)
    button.pack(pady=5)

    estados_label = ttk.Label(opcion3_window, text="Estados Recomendados:")
    estados_label.pack(pady=5)
    estados_text = tk.Text(opcion3_window, height=10, width=80)
    estados_text.pack(pady=5)
    configurar_colores(estados_text)

def actualizar_name_combobox_3(event):
    selected_business_id = business_id_var_3.get()
    name = dfBusiness.loc[dfBusiness["business_id"] == selected_business_id, "name"].values[0]
    name_var_3.set(name)

def actualizar_business_id_combobox_3(event):
    selected_name = name_var_3.get()
    business_id = dfBusiness.loc[dfBusiness["name"] == selected_name, "business_id"].values[0]
    business_id_var_3.set(business_id)

def enviar_request_3():
    business_id = business_id_var_3.get()
    if not business_id:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un Business ID")
        return

    url = "https://recomendacionestados-3bgweof3mq-uc.a.run.app"
    try:
        response = requests.post(url, json={'business_id': business_id})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo completar la solicitud: {e}")
        return

    try:
        json_response = response.json()
        
        # Mostrar estados recomendados
        estados_recomendados = json_response.get("estados_recomendados_para_el_negocio", [])
        estados_recomendados_text = json.dumps(estados_recomendados, indent=4, ensure_ascii=False)
        estados_text.delete(1.0, tk.END)
        estados_text.insert(tk.END, estados_recomendados_text)
    except json.JSONDecodeError:
        messagebox.showerror("Error", "No se pudo decodificar la respuesta como JSON")
        estados_text.delete(1.0, tk.END)

root = tk.Tk()
root.title("Aplicación Principal")
root.configure(bg=BG_COLOR)
root.attributes("-toolwindow", True)

aplicar_estilos()

btn1 = ttk.Button(root, text="Recomendar Usuarios por Business ID", command=mostrar_recomendaciones)
btn1.pack(pady=10)

btn2 = ttk.Button(root, text="Predicción de Éxito", command=mostrar_prediccion_exito)
btn2.pack(pady=10)

btn3 = ttk.Button(root, text="Recomendación de Estados", command=opcion3)
btn3.pack(pady=10)

root.mainloop()
