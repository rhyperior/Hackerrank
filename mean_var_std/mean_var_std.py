import numpy as np

import functools

def calculate(nums):
  try:
        # To evalute whether the list encompasses all Integers.
        all_integers = functools.reduce(lambda x, y: x and y , list(map(lambda x: isinstance(x, int), nums)))
        
        if(len(nums) != 9 or not all_integers):
            raise ValueError('List must contain nine numbers.')
        
        result = {}
        b = np.array(nums).reshape((3,3))
        print(b.shape)
        i = 0
        # print(b)
        for i in range(0, b.shape[0]):
            if not 'mean' in result:
                result['mean'] = [[], []]
                result['variance'] = [[], []]
                result['standard deviation'] = [[], []]
                result['max'] = [[], []]
                result['min'] = [[], []]
                result['sum'] = [[], []]
            result['mean'][0].append(np.mean(b[:, i]))
            result['variance'][0].append(np.var(b[:, i]))
            result['standard deviation'][0].append(np.std(b[:, i]))
            result['max'][0].append(np.max(b[:, i]))
            result['min'][0].append(np.min(b[:, i]))
            result['sum'][0].append(np.sum(b[:, i]))

        for i in range(0, b.shape[1]):
            result['mean'][1].append(np.mean(b[i, :]))
            result['variance'][1].append(np.var(b[i, :]))
            result['standard deviation'][1].append(np.std(b[i, :]))
            result['max'][1].append(np.max(b[i, :]))
            result['min'][1].append(np.min(b[i, :]))
            result['sum'][1].append(np.sum(b[i, :]))
            # print(np.mean(b[:, i]))
        
        b.reshape((9,)) # Flattening the numpy array.

        result['mean'].append(np.mean(b))
        result['variance'].append(np.var(b))
        result['standard deviation'].append(np.std(b))
        result['max'].append(np.max(b))
        result['min'].append(np.min(b))
        result['sum'].append(np.sum(b))


        # print('all done', result)
        return result
  except ValueError as e:
      raise ValueError(e)

  except Exception as e:
      print('Exception in calculate fn', repr(e))