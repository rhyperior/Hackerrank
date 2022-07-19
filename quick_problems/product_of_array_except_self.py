"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""
from math import prod
from time import sleep
from typing import List
import timeit

def productExceptSelf(nums: List[int]) -> List[int]:
    try:
        left_prod = []
        right_prod = []
        result_list = []
        product = 1
        for item in nums:
            left_prod.append(product)
            product = left_prod[-1] * item 

        product = 1

        for _, item in enumerate(reversed(nums)):
            right_prod.insert(0, product)
            product = product * item
        
        for i in range(len(nums)):
            result_list.append(left_prod[i]*right_prod[i])
        
        print("done")
        return result_list
    except Exception as e:
        print("error in productExceptSelf fn", str(e))

if __name__=="__main__":
    start = timeit.default_timer()
    num_list = [-1,1,0,-3,3]
    # num_list = [1,2,3,4]

    output_list = productExceptSelf(nums=num_list)

    print(output_list)
    print(timeit.default_timer()-start)