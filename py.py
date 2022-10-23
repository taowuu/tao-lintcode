class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        # 递归二分
        return self.binary_search(nums, 0, len(nums) - 1, target)
    
    def binary_search(self, nums, start, end, target):
        # 递归出口
        if start > end:
            return -1
        # 二分
        mid = (start + end) / 2
        # 找到目标
        if nums[mid] == target:
            return mid
        # 目标过大
        if nums[mid] < target:
            return self.binary_search(nums, mid + 1, end, target)
        # 目标过小
        return self.binary_search(nums, start, mid - 1, target)
        