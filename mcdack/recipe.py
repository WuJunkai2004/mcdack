import json

from mcdack.metadata import *

def _get_item_id(item):
    if hasattr(item, "id"):
        return item.id()
    return item


class crafting:
    def __init__(self, shape):
        '''# Crafting recipe'''
        if not shape:
            raise ValueError("No shape provided")
        self.shape = shape
        self.type = "crafting_shapeless"
        if(len(shape) and 
          (type(shape[0]) == list or type(shape[0]) == tuple)):
            self.type = "crafting_shaped"
        
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
        if self.type == "crafting_shapeless":
            pattern, item_map = self._shapeless()
        else:
            pattern, item_map = self._shaped()

    def _shaped(self):
        item_map = {}
        char = ord('A')
        pattern = []
        for row in self.shape:
            line = ""
            for item in row:
                item_id = _get_item_id(item)
                if item_id not in item_map:
                    item_map[item_id] = chr(char)
                    char += 1
                if item_id != None:
                    line += item_map[item_id]
                else:
                    line += " "
            pattern.append(line)
        for other_line in range(3 - len(pattern)):
            pattern.append("   ")
        return pattern, item_map


class stonecutting:
    pass



class smelting:
    pass


if __name__ == "__main__":
    crafting([
        [block.stone, block.stone, block.stone],
        
    ]).to(
        block.stone_bricks, 1
    ).finish()
