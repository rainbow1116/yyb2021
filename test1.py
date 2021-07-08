import pandas as pd
import numpy as np

test = pd.DataFrame({'id':['1', '2', '3', '4'], 'value':[54, 56, 87, 21]})

test['value'] = np.round(test['value']/3, 2)

class Tree(object):
    def __init__(self, x, y, obj):
        self.x = x
        self.y = y
        self.obj = obj

    def build_tree(self, m):
        res = self.x + self.y + m + self.obj.lr
        return res

if __name__ == '__main__':
    tre = Tree(1, 2)
    res = tre.build_tree(3)
    print(res)