import IOsql

class Models():
    def __init__(self, config_path=r'C:\Users\lin\Desktop\data\program\product\online_log\db\config.json'):
        self.db = IOsql.IOsql(config_path)
        self.cursor = self.db.cursor
        self.reset_data()
    def reset_data(self):
        try:
            self.categories= self.get_all_categories()
            self.authors= self.get_authors()
        except Exception as e:
            print(f"Error resetting data: {e}")
    def get_all_categories(self):
        try:
            query = "SELECT * FROM category;"
            return self.db.execute_query(query)
        except Exception as e:
            print(f"Error retrieving categories: {e}")
            return None
    def get_authors(self, limit=1)->int:
        
        try:
            target=self.db.config.other['author_name']
            query = "SELECT * FROM author  WHERE author_name=%s LIMIT %s;"
            o=self.db.execute_query(query,(target,limit))[0]
            o={'author_id':o[0],'author_name':o[1]}
            return o
        except Exception as e:
            print(f"Error retrieving authors: {e}")
            return 

def debug():
    models = Models()
    print("Categories:", models.categories)
    print("Authors:", models.authors)
    print(models.db.config.other['author_name'])
    return models

if __name__ == "__main__":
    debug()