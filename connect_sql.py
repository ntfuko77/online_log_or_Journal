import json
import mysql.connector

class config:
    def __init__(self, config_path='config.json'):
        self.config = self.load_sql_config(config_path)
        for i in ['host', 'user', 'password', 'database']:
            if i not in self.config:
                raise KeyError(f"Missing required config key: {i}")
        if type(self.config) is not dict:
            raise TypeError("Config file must contain a JSON object.")
        
        print("SQL configuration loaded successfully.")

    def get(self, key, default=None):
        return self.config.get(key, default)
    def load_sql_config(self,config_path='sql_config.json'):
        with open(config_path, 'r') as file:
            config = json.load(file)
        return config
    def __repr__(self):
        return f"SQL Config: {type(self.config)}:{self.config}"
class connect_sql:
    def __init__(self, config):
        self.config = config
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor() if self.connection else None

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.config.get('host'),
                user=self.config.get('user'),
                password=self.config.get('password'),
                database=self.config.get('database')
            )
            print("Connection to MySQL database established successfully.")
            return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def __exit__(self):
        if self.connection:
            self.connection.close()
            print("MySQL connection closed.")

sql_config = config()
db_connection = connect_sql(sql_config)
db_connection.cursor.execute("SELECT * FROM test_ringo LIMIT 5;")
results = db_connection.cursor.fetchall()
print(results)