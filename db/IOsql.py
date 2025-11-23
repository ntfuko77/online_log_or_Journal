from .connect_sql import Config, Connect_sql

class IOsql:
    def __init__(self, config_path='config.json'):
        self.config = Config(config_path)
        self.db_connection = Connect_sql(self.config)
        self.cursor = self.db_connection.cursor

    def execute_query(self, query,params=None):
        if self.cursor:
            self.cursor.execute(query,params or ())
            return self.cursor.fetchall()
        else:
            print("No database connection available.")
            return None
    @property
    def state(self):
        return {'config_status':self.config.config_load_status,
                'connection_status':self.db_connection.connection_status}