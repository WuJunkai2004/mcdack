import json

from mcdack.metadata import *

def _get_item_id(item):
    if hasattr(item, "id"):
        return item.id()
    return item

def _get_item_type(item):
    if hasattr(item, "type") and item.type() != "block":
        return item.type()
    return "item"


class crafting:
    def __init__(self, shape):
        '''# Crafting recipe'''
        if not shape:
            raise ValueError("No shape provided")
        self.shape = shape
        self.type = "minecraft:crafting_shapeless"
        if(len(shape) and 
          (type(shape[0]) == list or type(shape[0]) == tuple)):
            self.type = "minecraft:crafting_shaped"
        self.result = None
        self.result_count = 1
        self.group = None
    
    def group(self, group):
        self.group = group
        return self

    def to(self, result, count = 1):
        self.result = result
        self.result_count = count
        return self
    
    def finish(self):
        file_name = str(id(self)) + ".json"
        result = {
            'type': self.type,
            'result': {
                'item': _get_item_id(self.result),
                'count': self.result_count
            }
        }
        if self.group:
            result['group'] = self.group
        if self.type == "crafting_shapeless":
            pattern = self._shapeless()
            result['ingredients'] = pattern
        else:
            pattern, item_map = self._shaped()
            result['pattern'] = pattern
            result['key'] = item_map
        with open(file_name, 'w') as file:
            json.dump(result, file, indent=4)

    def _shaped(self):
        item_map = {}
        keys_map = {}
        char = ord('A')
        pattern = []
        for row in self.shape:
            line = ""
            for item in row:
                item_id = _get_item_id(item)
                if item_id not in item_map:
                    item_map[item_id] = chr(char)
                    keys_map[chr(char)] = { _get_item_type(item): item_id }
                    char += 1
                if item_id != None:
                    line += item_map[item_id]
                else:
                    line += " "
            pattern.append(line)
        for other_line in range(3 - len(pattern)):
            pattern.append("   ")
        return pattern, keys_map
    
    def _shapeless(self):
        pattern = []
        for item in self.shape:
            pattern.append({ _get_item_type(item): _get_item_id(item) })
        return pattern


class stonecutting:
    pass



class smelting:
    pass
