#two sum array
# Runtime 1060 ms Beats 33.5%
# Memory 14.9 MB Beats 73.43%

nums = [3,2,4,0]
# integer target
target = 6
# determine the difference between the target and first number in nums
# if the value of the first number returns another number in the list, return index of the first number
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index =[]
        for index in range(len(nums)):
            temp =nums[index]
            nums[index] = None
            if (target -temp) in nums:
                num_index.append(index)
            nums[index] = temp
        return num_index

results = Solution().twoSum([0,2,4,5,6,9],7)
print(results)