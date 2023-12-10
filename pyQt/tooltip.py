import sys
from PyQt6.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt6.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 设置字体
        QToolTip.setFont(QFont('SansSerif', 10))
        # 设置工具提示
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 创建按钮对象
        btn = QPushButton('Button', self)
        # 设置工具提示
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 设置按钮图形大小
        btn.resize(50, 50)
        # 设置按钮位置
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


def main():
    app = QApplication(sys.argv)
    Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
