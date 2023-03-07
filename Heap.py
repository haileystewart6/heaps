class Heap:
    def __init__(self, key=lambda x:x):
        self.data = []
        self.key  = key

    @staticmethod
    def _parent(idx):
        return (idx-1)//2
        
    @staticmethod
    def _left(idx):
        return idx*2+1

    @staticmethod
    def _right(idx):
        return idx*2+2
    
    def heapify(self, idx=0):
        while True:
            right = Heap._right(idx)
            left = Heap._left(idx)
            max_idx = idx
            if max_idx != idx:
                self.data[idx], self.data[max_idx] = self.data[max_idx],self.data[idx]
                idx = max_idx
            if left < len(self) and self.key(self.data[left]) > self.key(self.data[idx]):
                max_idx = left
            if right < len(self) and self.key(self.data[right]) > self.key(self.data[max_idx]):
                max_idx= right
            else:
                   break  

    def add(self, x):
        self.data.append(x)
        temp = len(self.data)-1
        temp2 = Heap._parent(temp)
        while temp > 0 and self.key(self.data[temp2]) < self.key(self.data[temp]):
            self.data[temp], self.data[temp2] = self.data[temp2], self.data[temp]
            temp = temp2
            temp2 = Heap._parent(temp)
        
    def peek(self):
        return self.data[0]

    def pop(self):
        value = self.data[0]
        self.data[0] = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        self.heapify()
        return value
    
    def __bool__(self):
        return len(self.data) > 0

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)
