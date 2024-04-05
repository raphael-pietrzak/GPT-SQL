import json
import sqlite3


class JsonToDb:
    """
    The JsonToDb class creates a table in a SQLite database from a JSON file.

    Args:
        json_file_path (str): The path to the JSON file.
        db_path (str): The path to the SQLite database.
        table_name (str): The name of the table to create in the database.

    Attributes:
        json_file_path (str): The path to the JSON file.
        db_path (str): The path to the SQLite database.
        table_name (str): The name of the table to create in the database.
        data (dict): The JSON data extracted from the file.
        headers (list): The column headers of the table, inferred from the JSON keys.

    Methods:
        read_json(): Reads the JSON file and returns its content as a dictionary.
        create_table(): Creates the table if it does not exist.
        get_headers(): Extracts the column headers from the JSON dictionary keys.
        insert_into_db(): Inserts the JSON data into the table.
    """

    def __init__(self, json_file_path, db_path, table_name):
        self.json_file_path = json_file_path
        self.db_path = db_path
        self.table_name = table_name
        self.data = self.read_json()
        self.headers = self.get_headers()

    def read_json(self):
        try:
            with open(self.json_file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("Le fichier spécifié est introuvable.")
            return None
        except json.JSONDecodeError:
            print("Erreur lors de la lecture du fichier JSON.")
            return None

    def create_table(self):
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            columns_str = ", ".join(f"{header} TEXT" for header in self.headers)
            sql_query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({columns_str})"
            c.execute(sql_query)
        except sqlite3.Error as e:
            print("Erreur lors de l'insertion des données dans la base de données :", e)

    def get_headers(self):
        return list(self.data[0].keys())

    def insert_into_db(self):
        self.create_table()
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            colums = ", ".join(f"{header}" for header in self.headers)
            for entry in self.data:
                sql_query = f"INSERT INTO {self.table_name} ({colums}) VALUES {tuple(entry.values())}"
                c.execute(sql_query)
            conn.commit()
            conn.close()
            print("Données insérées avec succès dans la base de données.")
        except sqlite3.Error as e:
            print("Erreur lors de l'insertion des données dans la base de données :", e)
