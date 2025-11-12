import IOsql

class entity():
    def __init__(self,data,description:list,author_dict:dict,people_dict:dict,empty=False):
        if isinstance(description[0],tuple):
            description=[i[0] for i in description]
        elif empty:
            description=description[0]
        try:
            for i in range(len(description)):
                setattr(self,description[i],data[i])
            if empty:return
            self.author_name=author_dict.get(self.author_id,'Unknown Author')
            self.people_name=people_dict.get(self.people_id,'Unknown Person')
        except Exception as e:
            print(f"Error initializing entity: {e}")
    @classmethod
    def empty(cls):
        description=['content','start_time', 'author_name', 'related_people', 'activity', 'location']
        return cls([None for i in range(len(description))],[description],{},{},True)

    def __repr__(self):
        return f"Entity({self.__dict__})"
    



class ModelService():
    
    def __init__(self, config_path):
        self.db = IOsql.IOsql(config_path)
        self.cursor = self.db.cursor
        self.reset_data()
    def reset_data(self):
        try:
            self.categories= self.get_all_categories()
            self.author= self.get_author()
            self.people= self.get_all_people(self.author['author_id'])
        except Exception as e:
            print(f"Error resetting data: {e}")
    def get_all_categories(self):
        try:
            query = "SELECT * FROM category;"
            return self.db.execute_query(query)
        except Exception as e:
            print(f"Error retrieving categories: {e}")
            return None
    def get_author(self, limit=1)->dict:
        try:
            target=self.db.config.other['author_name']
            query = "SELECT * FROM author  WHERE author_name=%s LIMIT %s;"
            o=self.db.execute_query(query,(target,limit))[0]
            o={'author_id':o[0],'author_name':o[1]}
            return o
        except Exception as e:
            print(f"Error retrieving authors: {e}")
            return 
    def get_all_people(self,author_id:int):
        try:
            query = "SELECT * FROM people WHERE author_id=1 or author_id=%s;"
            row=self.db.execute_query(query,(author_id,))
            for i in row:
                out={i[0]:i[1]}
            return out
        except Exception as e:
            print(f"Error retrieving all people: {e}")
            return None
    def get_entity_by_author(self):
        try:
            query = "SELECT * FROM entity WHERE author_id=%s;"
            row=self.db.execute_query(query,(self.author['author_id'],))
            return [entity(i,self.db.cursor.description,self.author,self.people) for i in row]
        except Exception as e:
            print(f"Error retrieving entities by author: {e}")
            return None
class Models():
    def __init__(self, config_path):
        pass
def debug():
    models = ModelService(r'db\config.json')
    # print("Categories:", models.categories)
    # print("Authors:", models.author)
    # print("People:", models.people)
    # print(models.db.config.other['author_name'])
    print("Entities by Author:", models.get_entity_by_author())
    print("empty entity:", entity.empty())
    
    return models

if __name__ == "__main__":
    debug()