import sys
import threading
from datetime import datetime, timedelta

from PySide6.QtCore import QTimer, QTime
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_demo import Ui_MainWindow
from time import sleep
from control_sending import ControlSending
from Signal import my_signal


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()  # UI类的实例化()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.bind()

    def confirm(self):
        my_signal.setProgressBar.emit(0)
        my_signal.setProgressBar_2.emit(0)
        # 创建一个子线程执行 延时时间进度条显示
        delayed_thread = threading.Thread(target=self.send_msg)
        delayed_thread.daemon = True  # 设置该线程为守护线程
        delayed_thread.start()  # 开启线程

    def bind(self):
        self.ui.pushButton.clicked.connect(self.confirm)
        my_signal.setProgressBar.connect(self.set_progressBar)
        my_signal.setProgressBar_2.connect(self.set_progressBar_2)
        my_signal.setLabel_7.connect(self.set_label_7)
        my_signal.setLabel_9.connect(self.set_label_9)

    def set_label_7(self, time_str: str):
        self.ui.label_7.setText(time_str)

    def set_label_9(self, time_str: str):
        self.ui.label_9.setText(time_str)

    def set_progressBar_2(self, progress: int):
        self.ui.progressBar_2.setValue(progress)

    def set_progressBar(self, progress: int):
        self.ui.progressBar.setValue(progress)

    def send_msg(self):
        self.show_delayed_progress()
        cs = ControlSending(
            data=self.ui.textEdit.toPlainText(),  # 获取输入内容的文本信息
            somebody=self.ui.lineEdit.text(),  # 获取输入名字的信息
            count=self.ui.spinBox.value(),  # 获取循环次数信息
            time_cost=self.ui.timeEdit.text()  # 获取延迟时间信息
        )
        cs.send_data()

    def update_time(self):
        # self.ui.label_7.setText(QTime.currentTime().toString('hh:mm:ss'))
        my_signal.setLabel_7.emit(QTime.currentTime().toString('hh:mm:ss'))

    def show_delayed_progress(self):
        # 获取延时时间
        time_cost = self.ui.timeEdit.text()
        sum_second = int(time_cost[-2:]) + int(time_cost[3:5]) * 60 + int(time_cost[:2]) * 3600
        print(sum_second)
        # 计算发送时间
        time_2 = datetime.strptime(time_cost, '%H:%M:%S')
        total_time = (datetime.strptime(self.ui.label_7.text(), '%H:%M:%S')
                      + timedelta(hours=time_2.hour, minutes=time_2.minute, seconds=time_2.second))
        # self.ui.label_9.setText(str(total_time.strftime('%H:%M:%S')))
        #
        my_signal.setLabel_9.emit(str(total_time.strftime('%H:%M:%S')))
        for i in range(sum_second):
            sleep(1)
            progress = (i + 1) * 100 // sum_second
            # self.ui.progressBar_2.setValue(progress)
            my_signal.setProgressBar_2.emit(progress)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    sys.exit(app.exec())  # 避免程序执行到这一行后直接退出
