# 在前 1 个数组中查找1
range_total = 1
# 查找范围倍增
while reader.get(range_total - 1) < target:
    range_total *= 2
# 二分模板
start, end = 0, len(range_total) - 1

while start + 1 < end:
    mid = (start + end) / 2

    if reader.get(mid) < target:
        start = mid
    else:
        end = mid
# 寻找第一次出现的位置所以先判断 start
if reader.get(start) == target:
    return start
if reader.get(end) == target:
    return end
    
return -1