from rich.console import Console
from rich.table import Table
from db import models
#- external dependency:rich

class EntityTable:
    def __init__(self,entity):
        self.entity=entity
    def to_rich_table(self):
        entity_id=getattr(self.entity,'entity_id','N/A')
        table=Table(title=f'Entity ID: {entity_id}',show_header=True, header_style="bold magenta")
        value={'description':[],'value':[]}
        value['description'].extend(['content','start_time', 'author_name', 'related_people', 'activity', 'location'])
def debug():
    mod = models.Models(r'db\config.json')
    data=mod.service.get_entity_by_author()

    console=Console()
    table=Table(title='event',show_header=True, header_style="bold magenta")


    print(data[0])

if __name__ == "__main__":
    debug()