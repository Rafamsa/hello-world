from pathlib import Path  # Path trabalha com manipulação de arquivos

import requests  # faz requisições (pedir algo para a internet) http
import psycopg  # camada de conexão com o banco de dados (só postgres)


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


def get_sql(file):
    base_dir = (
        Path.cwd()
    )  # cwd função que busca a pasta que está usando atualmente | cwd = Current working dir
    file_path = base_dir / file
    if not file_path.exists():
        raise ValueError("Arquivo não encontrado! :(")
    if not file_path.suffix == ".sql":
        raise ValueError("Arquivo SQL não encontrado! :(")


class User:  # "receita de objetos"
    def list(self):
        response = requests.get(
            "https://697b4b380e6ff62c3c5b9ac0.mockapi.io/api/v1/users"
        )
        return response.json()

    def get(self):
        raise NotImplementedError

    def save(self): ...  # ... = pass = não fazer nada


get_sql("eu.sql")

"""def def()
    print("abluble sei la")   PYTHON FRESCO NAO ME DEIXA DAR O NOME DA FUNÇÃO DE DEF (palavra reservada)"""
