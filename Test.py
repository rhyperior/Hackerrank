from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dict_a = {}
        result_set = set()
        result = []
        for num in nums:
            if num in dict_a:
                dict_a[num] += 1
            else:
                dict_a[num] = 1

        for index, i in enumerate(nums):
            for j in nums[index + 1 :]:
                composite = 0 - (i + j)

                composite_count = dict_a.get(composite, 0)

                if (composite, i, j) == (0, 0, 0) and composite_count < 3:
                    pass
                elif composite in (i, j) and composite_count > 1:
                    result_set.add(tuple(sorted([i, j, composite])))

                elif composite not in (i, j) and composite_count > 0:
                    result_set.add(tuple(sorted([i, j, composite])))

        for i in result_set:
            result.append(list(i))
        return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [1, 2, -2, -1]
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    nums = [-1, 0, 1, 0]
    print(Solution().threeSum(nums=nums))
