import requests
import psycopg

DATABASE = {
    "name": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432",
}  # constante, por isso letra maiuscula


def get_connection(**options):
    conninfo = f"dbname={options['name']} user={options['user']} password={options['password']} host={options['host']} port={options['port']}"
    return psycopg.connect(conninfo)


class User:  # "receita de objetos"
    def list(self):
        response = requests.get(
            "https://697b4b380e6ff62c3c5b9ac0.mockapi.io/api/v1/users"
        )
        return response.json()

    def get(self):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError


get_connection(**DATABASE)
