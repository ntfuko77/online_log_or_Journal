import rich
from db import models

def debug():
    mod = models.Models(r'db\config.json')
    data=mod.service.get_entity_by_author()
    print(data)
print(1)
if __name__ == "__main__":
    debug()