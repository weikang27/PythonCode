"""
TODO:
 Question:
  给定n种硬币的面值为coins[i-1],
  目标金额为amt,
  每种硬币可以重复选取,
  问能够凑出目标金额的最少硬币个数。
  如果无法凑出目标金额则返回-1.
"""

"""
coins= [1, 5, 10, 20]    n=4
i = 3 coins[2] = 10
amt = 30

20
10

lst = [19, 25, 20, 10]
"""


def change_exchange(coins: list[int], amt: int):
    """零钱兑换"""
    money = amt  # 当前金额
    while True:
        dic = {}  # 空字典
        for i in range(len(coins)):
            if money - coins[i] >= 0:   # 找出所有可以选择的值
                dic.update({money - coins[i]: i})  # 添加到字典中
        print(f'当前字典值{dic}')
        # for i in lst:
        #     # 从面值中选择不大于且最接近它的硬币
        #     if i <= money and i - money:   # 找到一种面值小于或等于金额
        #         print(f'当前选择的是:{i}面值硬币')
        #         money = money - i
        # 获取最小值索引
        # print(f"当前最小的key:{min(dic)}")
        index = dic.get(min(dic))
        print(f'当前选择的是:{coins[index]}面值硬币')
        money = money - coins[index]
        if money == 0:
            return
change_exchange([1, 5, 10, 50, 20, 100], 254)
# change_exchange([1, 20, 50], 60)
