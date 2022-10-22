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
        # 临时数组存放结果
        temp = []
        mergeSort(a, 0, len(a) - 1, temp)
    
    def merge_sort(self, start, end, temp):
        # 递归终止条件
        if start >= end:
            return
        
        # 分别排序
        self.merge_sort(a, start, (start + end) / 2, temp)
        self.merge_sort(a, (start + end) / 2 + 1, end, temp)
        # 合并
        self.merge(a, start, end, temp)

    def merge(self, start, end, temp):
        # 定义分块的左右起点
        middle = (start + end) / 2 + 1
        left_index = start
        right_index = middle + 1
        # 临时数组的起点
        index = left_index
        对两分块分别取值排序
        while left_index <= middle and right_index <= end:
            if a[left_index] < a[right_index]:
                temp[index] = a[left_index]
                index += 1
                left_index += 1
            else:
                temp[index] = a[right_index]
                index += 1
                right_index += 1


