from . import IOsql

class entity():
    attr_name=['content','start_time', 'author_name', 'related_people', 'activity', 'location']
    #example Entity({'entity_id': 1, 'content': '寫程式使我興奮!', 'create_at': datetime.datetime(2025, 11, 4, 20, 16, 11), 
    # 'start_time': datetime.datetime(2025, 11, 4, 20, 16, 11), 'author_id': 2, 'related_people_id': None, 'activity': '剛剛同時和月和霧聊天', 
    # 'location': '家裡', 'author_name': 'Unknown Author'})
    def __init__(self,data,description:list,author_dict:dict,people_dict:dict,tag_dict:dict,category_dict:dict,empty=False):
        if isinstance(description[0],tuple):
            description=[i[0] for i in description]
        elif empty:
            description=description[0]
        try:
            for i in range(len(description)):
                setattr(self,description[i],data[i])
            if empty:return
            serch_key = getattr(self,"author_id",0)

            if author_dict.get("author_id",None)==serch_key:
                self.author_name=author_dict.get('author_name','Unknown Author')

            else:
                self.author_name='Unknown Author'



            serch_key = getattr(self,"people_id",0)
            if people_dict.get("people_id",None)==serch_key:
                self.people_name=people_dict.get('people_name','Unknown Person(not found)')
            else:
                self.people_name='Unknown Person'
            search_key = getattr(self,"tag_id",0)
            
            if search_key in tag_dict:
                self.tag_name=tag_dict.get(search_key,'Unknown Tag(not found)')
            else:
                self.tag_name='Unknown Tag'
            search_key = getattr(self,"category_id",0)
            print(f"Debug: category_id={getattr(self,'category_id',None)}, category_dict={category_dict}")

            if getattr(self,'category_id',0) in category_dict:
                self.category_name=category_dict.get(search_key,'Unknown Category(not found)')
            else:
                self.category_name='Unknown Category'

        except Exception as e:
            print(f"Error initializing entity: {e}")
            
    @classmethod
    def empty(cls):
        description=cls.attr_name
        return cls([None for i in range(len(description))],[description],{},{},{},True)

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
            self.tag= self.get_all_tags()
        except Exception as e:
            print(f"Error resetting data: {e}")
    def get_all_categories(self):
        try:
            query = "SELECT * FROM category;"
            row=self.db.execute_query(query)
            print(row)
            out={}
            for i in row:
                out[i[0]]=i[1]
            return out
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
    def get_all_tags(self):
        try:
            query = "SELECT * FROM tag;"
            row=self.db.execute_query(query)
            out={}
            for i in row:
                out[i[1]]=i[0]
            return out
        except Exception as e:
            print(f"Error retrieving all tags: {e}")
            return None
    def get_entity_by_author(self):
        try:
            query = "SELECT * FROM entity_with_tags WHERE author_id=%s;"
            row=self.db.execute_query(query,(self.author['author_id'],))
            return [entity(i,self.db.cursor.description,self.author,self.people,self.tag,self.categories) for i in row]
        except Exception as e:
            print(f"Error retrieving entities by author: {e}")
            return None
class ModelRespository():
    def __init__(self, cursor):
        self.cursor = cursor
    def push_tag(self, tag_name: str):
        ... # Implementation for pushing a tag to the database
    def push_category(self, category_name: str):
        ... # Implementation for pushing a category to the database
    def push_entity(self, entity_data: dict):
        ... # Implementation for pushing an entity to the database
    def delete_entity(self, entity_id: int):
        ... # Implementation for deleting an entity from the database


class Models():
    def __init__(self, config_path):
        self.service = ModelService(config_path)
    
def debug():
    models = Models(r'db\config.json')
    # print("Categories:", models.categories)
    # print("Authors:", models.author)
    # print("People:", models.people)
    # print(models.db.config.other['author_name'])
    print("Entities by Author:", models.service.get_entity_by_author())
    print("empty entity:", entity.empty())
    
    return models

if __name__ == "__main__":
    debug()