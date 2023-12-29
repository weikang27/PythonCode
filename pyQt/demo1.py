import sys
import time

from PyQt6.QtWidgets import (
    QApplication, QWidget, QMessageBox, QPushButton, QStyle
)


# TODO 确认按钮功能

# 创建实例类
class Example(QWidget):
    # 构造方法
    def __init__(self):
        # 调用父类构造
        super().__init__()
        self.initUI()

    # 初始化UI
    def initUI(self):
        # 设置主窗口大小，位置
        self.resize(400, 400)
        self.center()
        # 设置主标题
        self.setWindowTitle('First GUI')
        # 创建确认按钮
        btn = QPushButton(text='确认', parent=self)
        btn.move(20, 20)
        btn.resize(btn.sizeHint())
        # 设置显示
        self.show()

    # 设置窗口居中
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# 定义一个主方法用于启动
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
