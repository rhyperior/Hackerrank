import numpy as np

import functools
from typing import List, Dict

def calculate(nums : List[int]) -> Dict :
    try:
        # To evalute whether the list encompasses all Integers.
        all_integers = functools.reduce(lambda x, y: x and y , list(map(lambda x: isinstance(x, int), nums)))
        
        if(len(nums) != 9 or not all_integers):
            raise ValueError('List must contain nine numbers.')
        
        b = np.array(nums).reshape((3,3))
        print(b.shape)

        print('all done', all_integers)

    except ValueError as e:
        raise ValueError(e)
    except Exception as e:
        print('Exception in calculate fn', str(e))

if __name__=='__main__':
    # num_list = [1, 2, 3, 4, 5, 6, 7, 8, 'what\'s up G']
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    calculate(num_list)