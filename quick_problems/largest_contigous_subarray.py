"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Accepted
2,455,672
Submissions
4,948,876
"""
from typing import List

def largst_contigous_subarray(nums: List[int]) -> int:
    try:
        start_index = -1
        last_index = 0
        max = nums[0]
        moving_sum = 0
        sum = 0
        for num in nums:
            max = num if num > max else max
        
        if max < 0:
            return max

        for num in nums:
            moving_sum = moving_sum + num
            
            if moving_sum < 0:
                if moving_sum + sum < 0:
                    max = sum if sum > max else max
                    sum = 0
                    moving_sum = 0
            
            # if moving_sum > 0:     # This one line made the solution around 70% slower.
            else :
                sum = sum + moving_sum
                moving_sum = 0

        max = sum if sum > max else max

        return max

    except Exception as e:
        print("error in largest_contigous_subarray fn", str(e))

if __name__=="__main__":
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [1]
    nums = [5,4,-1,7,8]
    # nums = [1,-2,-2,-1]

    largest_sum = largst_contigous_subarray(nums=nums)

    print(largest_sum)
    # print('def')

