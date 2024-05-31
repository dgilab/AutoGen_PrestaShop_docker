import yaml
import subprocess

def main():
    bd = input("Ingrese el nombre del contenedor para MySQL: ").strip()
    presta = input("Ingrese el nombre del contenedor para PrestaShop: ").strip()
    php = input("Ingrese el nombre del contenedor para PhpMyAdmin: ").strip()
    dbuser = input("Ingrese el nombre de usuario para MySQL: ").strip()
    dbpass = input(f"Ingrese la contraseña para el usuario {dbuser}: ").strip()
    dbname = input("Ingrese el nombre de la Base de datos: ").strip()
    hnps = input("Ingrese HostName para prestashop: ").strip()
    hnphp = input("Ingrese HostName para PhPMyAdmin: ").strip()
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
    with open('docker-compose.yml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

    print("Archivo 'docker-compose.yml' generado con éxito.")

    # Ejecutar `docker-compose up --build`
    subprocess.run(["docker-compose", "up", "--build"])

if __name__ == "__main__":
    main()