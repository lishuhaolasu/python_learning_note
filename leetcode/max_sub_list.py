''' 和最大子数组
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''

import numpy
def max_sub_list(nums:[int,...]) -> int:
    # 定义要返回的值_sum和当前最大和now，值为第一个元素
    _sum = now = nums[0]
    # 定义起始元素下标
    start = end = 0
    # 从第二个元素开始遍历
    for k ,val in enumerate(nums):
        if k == 0:
            continue
        # 如果当前和仍大于0，则将下一个值加至now中
        if now > 0:
            now += val
            end = k
        # 如果当前和已经小于0了，则将now置为下一个元素。
        # 如果数组全为负值，则最小的肯定不会是和。如果中间有正数，当然是取正数更大，哪怕只有一个数
        else:
            now = val
            start = end = k
        # 如果最大和小于当前和，则将当前和赋值给最大和
        if _sum < now :
            _sum = now 
    print(start,end)
    return _sum

r_list = numpy.random.randint(-10,10,size=(100))
print(r_list)
sub_sum = max_sub_list(r_list)
print(sub_sum)
