import pandas as pd
import numpy as np

test = pd.DataFrame({'id':['1', '2', '3', '4'], 'value':[54, 56, 87, 21]})

test['value'] = np.round(test['value']/3, 2)

if __name__ == '__main__':
    print(test)