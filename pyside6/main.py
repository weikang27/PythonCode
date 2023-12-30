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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.bind()

    def confirm(self):
        my_signal.setProgressBar.emit(0)
        my_signal.setProgressBar_2.emit(0)

        delayed_thread = threading.Thread(target=self.send_msg)
        delayed_thread.daemon = True
        delayed_thread.start()

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
            data=self.ui.textEdit.toPlainText(),
            somebody=self.ui.lineEdit.text(),
            count=self.ui.spinBox.value(),
            time_cost=self.ui.timeEdit.text()
        )
        cs.send_data()

    def update_time(self):
        my_signal.setLabel_7.emit(QTime.currentTime().toString('hh:mm:ss'))

    def show_delayed_progress(self):
        time_cost = self.ui.timeEdit.text()
        sum_second = int(time_cost[-2:]) + int(time_cost[3:5]) * 60 + int(time_cost[:2]) * 3600
        print(sum_second)
        time_2 = datetime.strptime(time_cost, '%H:%M:%S')
        total_time = (datetime.strptime(self.ui.label_7.text(), '%H:%M:%S')
                      + timedelta(hours=time_2.hour, minutes=time_2.minute, seconds=time_2.second))
        my_signal.setLabel_9.emit(str(total_time.strftime('%H:%M:%S')))
        for i in range(sum_second):
            sleep(1)
            progress = (i + 1) * 100 // sum_second
            my_signal.setProgressBar_2.emit(progress)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
