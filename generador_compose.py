import tkinter as tk
from tkinter import ttk
import yaml
import subprocess

class PopupForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Formulario Docker Compose")
        self.geometry("400x600")

        self.entries = {}
        self.values = {}

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style(self)
        style.configure('TLabel', background='lightgrey', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12), background='lightblue', foreground='black')
        # Definir etiquetas y entradas
        fields = [
            "Nombre del contenedor para MySQL",
            "Nombre del contenedor para PrestaShop",
            "Nombre del contenedor para PhpMyAdmin",
            "Nombre de usuario para MySQL",
            "Contraseña para el usuario de MySQL",
            "Nombre de la Base de datos",
            "HostName para PrestaShop",
            "HostName para PhpMyAdmin"
        ]
        
        for field in fields:
            label = tk.Label(self, text=field + ":", font=('Arial', 12))
            label.pack(pady=5, padx=20, fill='x')
            entry = tk.Entry(self, font=('Arial', 12))
            entry.pack(pady=5, padx=20, fill='x')
            self.entries[field] = entry

        # Botón de enviar
        submit_button = tk.Button(self, text="Enviar", command=self.submit, font=('Arial', 12))
        submit_button.pack(pady=15)

    def submit(self):
        # Obtener valores de las entradas
        self.values['bd'] = self.entries["Nombre del contenedor para MySQL"].get()
        self.values['presta'] = self.entries["Nombre del contenedor para PrestaShop"].get()
        self.values['php'] = self.entries["Nombre del contenedor para PhpMyAdmin"].get()
        self.values['dbuser'] = self.entries["Nombre de usuario para MySQL"].get()
        self.values['dbpass'] = self.entries["Contraseña para el usuario MySQL"].get()
        self.values['dbname'] = self.entries["Nombre de la Base de datos"].get()
        self.values['hnps'] = self.entries["HostName para PrestaShop"].get()
        self.values['hnphp'] = self.entries["HostName para PhpMyAdmin"].get()

        # Llamar a la función main con los valores del formulario
        self.destroy()
        main(self.values)

def main(values):
    bd = values['bd']
    presta = values['presta']
    php = values['php']
    dbuser = values['dbuser']
    dbpass = values['dbpass']
    dbname = values['dbname']
    hnps = values['hnps']
    hnphp = values['hnphp']

    data = {
        "version": "3",
        "services": {
            presta: {
                "image": "prestashop/prestashop",
                "ports": ["8080:80"],
                "environment": {
                    "DB_SERVER": bd,
                    "DB_USER": dbuser,
                    "DB_PASSWD": dbpass,
                    "DB_NAME": dbname
                },
                "volumes": ["prestashop:/var/www/html"],
                "hostname": hnps
            },
            php: {
                "image": "phpmyadmin/phpmyadmin",
                "ports": ["8081:80"],
                "environment": {
                    "PMA_HOST": bd,
                    "MYSQL_ROOT_PASSWORD": dbpass
                },
                "hostname": hnphp
            },
            bd: {
                "image": "mysql:5.7",
                "environment": {
                    "MYSQL_DATABASE": dbname,
                    "MYSQL_USER": dbuser,
                    "MYSQL_PASSWORD": dbpass,
                    "MYSQL_ROOT_PASSWORD": dbpass
                },
                "volumes": ["db_data:/var/lib/mysql"],
            }
        },
        "volumes": {
            "prestashop": {},
            "db_data": {}
        }
    }

    try:
        with open('docker-compose.yml', 'w') as file:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False)
        print("Archivo 'docker-compose.yml' generado con éxito.")
    except Exception as e:
        print(f"Error al generar el archivo YAML: {e}")
    

    print("Archivo 'docker-compose.yml' generado con éxito.")

    try:
        subprocess.run(["docker-compose", "up", "--build"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar docker-compose: {e}")

if __name__ == "__main__":
    app = PopupForm()
    app.mainloop()