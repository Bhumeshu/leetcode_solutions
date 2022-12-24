class Solution:
    nums = 10

    def twosum(self, nums: list, target: int) -> [int]:
        for i in range(len(nums)-1):
            for x in range(i+1, len(nums)):
                if target - nums[i] == nums[x]:
                    return i, x
        return False


print(Solution.twosum([1, 2, 3], 4))
