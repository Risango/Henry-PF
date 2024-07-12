import tkinter as tk
from tkinter import messagebox
import requests
import json 

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
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, json.dumps(json_response, indent=4))
    except requests.exceptions.JSONDecodeError:
        messagebox.showerror("Error", "No se pudo decodificar la respuesta como JSON")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, response.text)

root = tk.Tk()
root.title("Business ID Recommender")

label = tk.Label(root, text="Ingrese Business ID:")
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Enviar", command=enviar_request)
button.pack(pady=5)

result_text = tk.Text(root, height=20, width=80)
result_text.pack(pady=5)

root.mainloop()
