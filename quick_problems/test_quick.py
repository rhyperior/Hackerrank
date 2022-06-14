import os
import functools
# import os.path
import operator

import datetime

from bisect import bisect
from bisect import bisect_left, bisect_right
from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         return 'abc'

from bisect import bisect_left

class Solution:
    def efficient_search(self, sorted_list: List[int], element: int):
        pos = bisect_left(sorted_list, element)
        if pos >= len(sorted_list) or sorted_list[pos]!=element:
            return False, -1
        return True, pos

    def find_original_pos(self, nums: List[int], sorted_nums: List[int], start_pos : int, last_pos : int):
        if start_pos >=0 and last_pos >=0:
            start_pos = nums.index(sorted_nums[start_pos])
            last_pos = nums.index(sorted_nums[last_pos])

            if start_pos == last_pos:
                position_list  =[]
                for item in range(len(nums)):
                    if nums[item] == nums[start_pos]:
                        position_list.append(item)
                start_pos = position_list[0]
                last_pos = position_list[1]
        return [start_pos, last_pos]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = nums[:]
        sorted_nums.sort()
        start_pos = -1
        last_pos = -1
        for item in range(len(sorted_nums)):
            find, pos = self.efficient_search(sorted_nums, target-sorted_nums[item])
            if find == True:
                last_pos = pos
                start_pos = item
                if last_pos == start_pos:
                    last_pos=last_pos+1
                break
        
        start_pos, last_pos = self.find_original_pos(nums, sorted_nums, start_pos, last_pos)
        return [start_pos, last_pos]
   

if __name__=="__main__":
    
    start_list = [2,7,11,15]
    # start_list = [3,2,3]
    # start_list = [3,3]
    start_list = [3,2,4]
    target = 6
    obj = Solution()
    pos = obj.twoSum(nums=start_list, target=target)

    print("done")