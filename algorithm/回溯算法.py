import math
import numpy as np

# 创建一个
arr = np.array([1, 2, 3])

# TODO 求从123中取出2个数的组合
#  12 13 23
# 方法一: combination （组合）
print(math.comb(3, 2))
# 方法二:
ans = []
#
# 方法三:

# TODO 求123中取出2个数的排序
#  12 21 31 13 23 32    math.perm(3, 2)
#
arr1 = np.array([1, 2, 3])
ans1 = []
# 利用递归思想求解问题
"""

"""
def func1(array: list):
    if array == []:
        return
    for i in array:
        ans1.append(i)
        array.remove(i)

