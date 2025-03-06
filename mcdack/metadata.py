''''''


class _meta:
    def __init__(self, type, name):
        self._type = type
        self._name = name
        self._data = {}

    def id(self):
        return self._name
    
    def type(self):
        return self._type
    
    def __call__(self, *args, **kwargs):
        self._data = kwargs
        return
    
    def nbt(self):
        nbt = self.data
        self._data = {}
        return nbt
    

class _block:
    def __init__(self, file):
        self._file = file
        with open(file, 'r') as f:
            for line in f:
                block_id = line.strip()
                setattr(self, block_id, _meta('block', block_id))

block = _block('mcdack/raw/block_id.txt')