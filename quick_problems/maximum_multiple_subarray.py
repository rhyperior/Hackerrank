"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List

def max_multiple(nums: List[int]) -> int:
    try:

        multiple = 1
        running_multiple = 1
        MAX = 0
        complete_product = 1
        total_sum = 0
        for item in nums:
            complete_product*=item
            total_sum+=item
        
        if total_sum <=0 and complete_product ==0:
            return 0

        for item in nums:
            running_multiple = running_multiple * item

            if running_multiple >= 1:
                multiple = multiple * running_multiple
                running_multiple = 1

            if running_multiple == 0:
                MAX = multiple
                multiple = 1
                running_multiple = 1
        
        MAX = multiple if multiple > MAX else MAX

        return MAX
    except Exception as e:
        print("error in max_multiple fn", str(e))

if __name__=="__main__":
    # nums = [2,3,-2,4]
    # nums = [-2,0,-1]
    nums = [-2]

    result = max_multiple(nums=nums)

    print(result)