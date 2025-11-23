from rich.console import Console
from rich.table import Table
from rich.pretty import Pretty
from db import models
#- external dependency:rich

class EntityTable:
    base_attr=['category_name','content','start_time','author_name','tag_name']
    extra_attr=['related_people','activity','location']
    column=['Description','Value']
    upper_row_width={'Description':20,'Value':30,'Extra Value':10}
    column_number=2
    def __init__(self):...
        
    @classmethod
    def entity_pretable(cls,entity):
        title=getattr(entity,'entity_id','N/A')
        table=Table(title=f'Entity ID: {title}',show_header=True, header_style="bold magenta")
        table.add_column("Description", style="dim", width=cls.upper_row_width['Description'])
        table.add_column("Value", style="dim", width=cls.upper_row_width['Value'])
        # table.add_column("Extra Value", style="dim", width=cls.upper_row_width['Extra Value'])
        for i in cls.base_attr:
            value=str(getattr(entity,i,'N/A'))
            row=[i,value]
            if cls.column_number==3:
                row.append('')
            table.add_row(*row)
        for i in cls.extra_attr:
            value=str(getattr(entity,i,'N/A'))
            if value!='N/A' and value!='None':
                row=[i,value]
                if cls.column_number==3:
                    row.append('')
                table.add_row(*row)
        return table
    @classmethod
    def to_rich_table(cls,data):
        if type(data)==models.entity:
            view=EntityTable.entity_pretable(data)
            return view

def tag_table(data):
    table=Table(title='Tags',show_header=True, header_style="bold magenta")
    table.add_column("Tag ID", style="dim", width=12)
    table.add_column("Tag Name", style="dim", width=30)
    for i in data:
        table.add_row(str(i),str(data[i]))
    return table

def debug():
    mod = models.Models(r'db\config.json')
    data=mod.service.get_entity_by_author()

    console=Console()
    table=EntityTable.to_rich_table(data[0])
    console.print(table)
    table=tag_table(mod.tag)
    console.print(table)



if __name__ == "__main__":
    debug()