from uiautomation import WindowControl  # 引入uiautomation库中的WindowControl类，用来进行图像识别和模拟操作
from Signal import my_signal


class ControlSending():
    # 有参构造方法
    def __init__(self, data: str, somebody: str, count: int, time_cost: str):
        self.data = data
        self.somebody = somebody
        self.count = count
        self.time_cost = time_cost

    # 发送消息函数
    def send_data(self):
        # 绑定微信主窗口
        wx = WindowControl(
            Name='微信',
            searchDepth=1
        )
        # 切换窗口
        wx.ListControl()
        wx.SwitchToThisWindow()
        # 寻找会话控件绑定
        hw = wx.ListControl(Name='会话')
        # Ctrl + F 查找某人
        wx.SendKeys('{Ctrl}{F}', waitTime=1)
        wx.SendKeys(f'{self.somebody}', waitTime=1)
        wx.SendKeys('{Enter}', waitTime=1)
        # 循环发送数据
        for i in range(self.count):
            wx.SendKeys(self.data.replace('\n', '{Shift}{Enter}') + '{Enter}')
            progress = (i + 1) * 100 // self.count
            my_signal.setProgressBar.emit(progress)


if __name__ == '__main__':
    cs = ControlSending(data='你好', somebody='#idol', count=2, time_cost='1:11')
    cs.send_data()
