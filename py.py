class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers(self, a):
        # write your code here
        # 边界判断
        if not a or len(a) == 0:
            return
        # 新数组存放结果
        temp = []
        mergeSort(a, 0, len(a) - 1, temp)
    
    def merge_sort(self, start, end, temp):
        # 递归终止条件
        if start >= end:
            return
        
        # 分别排序
        slef.merge_sort(a, start, (start + end) / 2, temp)
        slef.merge_sort(a, (start + end) / 2 + 1, end, temp)
        # 合并
        slef.merge(a, start, start, (start + end) / 2, end, temp)
        # 

