from sklearn.datasets import load_iris


def datasets_demo():
    """
    sklearn数据集使用
    """
    # 获取数据集
    iris = load_iris()
    print("鸢尾花数据集:\n", iris)
    print("查看数据集描述:\n", iris["DESCR"])
    print("查看特征值:\n", iris.data, iris.data.shape)


datasets_demo()
