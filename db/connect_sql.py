import json
import mysql.connector
#external dependency:mysql-connector-python



class Config:
    def __init__(self, config_path='config.json'):
        self.config = self.load_sql_config(config_path)
        if 'sql_connect' in self.config:
            self.other =  self.config['other_settings'] if 'other_settings' in self.config else {}
            self.config = self.config['sql_connect']

        else:
            raise KeyError("Missing 'sql_connect' section in config file.")
        for i in ['host', 'user', 'password', 'database']:
            if i not in self.config:
                raise KeyError(f"Missing required config key: {i}")
        if type(self.config) is not dict:
            raise TypeError("Config file must contain a JSON object.")
        
        print("SQL configuration loaded successfully.")

    def get(self, key, default=None):
        return self.config.get(key, default)
    def load_sql_config(self,config_path):
        try:
            with open(config_path, 'r') as file:
                config = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found: {config_path}")
        return config
    def __repr__(self):
        return f"SQL Config: {type(self.config)}:{self.config}"
class Connect_sql:
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
                database=self.config.get('database'),
                port=self.config.get('port', 3306)
            )
            print("Connection to MySQL database established successfully.")
            return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def __exit__(self):
        if self.connection:
            self.cursor.close()
            print("MySQL cursor closed.",end='')
            self.connection.close()
            print("MySQL connection closed.")

# sql_config = Config()
# db_connection = Connect_sql(sql_config)
# db_connection.cursor.execute("SELECT * FROM category LIMIT 5;")
# results = db_connection.cursor.fetchall()
# print(results)