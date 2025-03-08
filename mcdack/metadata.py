''''''


class _data:
    def __init__(self, type, name):
        self._type = type
        self._name = name
        self._data = {}

    def id(self):
        return f'minecraft:{self._name}'
    
    def type(self):
        return self._type
    
    def __call__(self, *args, **kwargs):
        self._data = kwargs
        return
    
    def nbt(self):
        nbt = self.data
        self._data = {}
        return nbt
    

class _dataset:
    def __init__(self, file, type):
        self._file = file
        self._type = type
        f = open(file, 'r')
        for line in f:
            name = line.strip()
            setattr(self, name, _data(type, name))
        f.close()


block = _dataset('raw/block_id.txt', 'block')
item  = _dataset('raw/item_id.txt',  'item')