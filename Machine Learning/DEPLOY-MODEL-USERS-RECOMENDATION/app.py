import tkinter as tk
from tkinter import messagebox
import requests
import json

def mostrar_recomendaciones():
    global entry, negocio_text, usuarios_text

    recomendador_window = tk.Toplevel(root)
    recomendador_window.title("Business ID Recommender")

    label = tk.Label(recomendador_window, text="Ingrese Business ID:")
    label.pack(pady=5)

    entry = tk.Entry(recomendador_window, width=50)
    entry.pack(pady=5)

    button = tk.Button(recomendador_window, text="Enviar", command=enviar_request)
    button.pack(pady=5)

    negocio_label = tk.Label(recomendador_window, text="Información del Negocio:")
    negocio_label.pack(pady=5)
    negocio_text = tk.Text(recomendador_window, height=10, width=80)
    negocio_text.pack(pady=5)

    usuarios_label = tk.Label(recomendador_window, text="Usuarios Recomendados:")
    usuarios_label.pack(pady=5)
    usuarios_text = tk.Text(recomendador_window, height=20, width=80)
    usuarios_text.pack(pady=5)

def enviar_request():
    business_id = entry.get()
    if not business_id:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un Business ID")
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
        negocio_info_text = json.dumps(negocio_info, indent=4)
        negocio_text.delete(1.0, tk.END)
        negocio_text.insert(tk.END, negocio_info_text)

        # Mostrar usuarios recomendados
        usuarios_recomendados = json_response.get("usuarios_recomendados", [])
        usuarios_recomendados_text = json.dumps(usuarios_recomendados, indent=4)
        usuarios_text.delete(1.0, tk.END)
        usuarios_text.insert(tk.END, usuarios_recomendados_text)
    except requests.exceptions.JSONDecodeError:
        messagebox.showerror("Error", "No se pudo decodificar la respuesta como JSON")
        negocio_text.delete(1.0, tk.END)
        usuarios_text.delete(1.0, tk.END)

def opcion2():
    # Aquí va el código para la opción 2
    pass

def opcion3():
    # Aquí va el código para la opción 3
    pass

root = tk.Tk()
root.title("Aplicación Principal")

btn1 = tk.Button(root, text="Recomendar Usuarios por Business ID", command=mostrar_recomendaciones)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Opción 2", command=opcion2)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Opción 3", command=opcion3)
btn3.pack(pady=10)

root.mainloop()
