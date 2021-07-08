import numpy as np
from test1 import Tree

test = np.array([1,2,3,4,5])

class yyb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lr = 0.05
    def fit(self, val):
        model = Tree(self.x, self.y, obj=self)
        tmp = model.build_tree(val)
        print(tmp)

if __name__ == '__main__':
    y1 = yyb(1, 2)
    res = y1.fit(val=2)
    print(res)