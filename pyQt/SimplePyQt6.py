import sys
from PyQt6.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 200)
    w.move()

    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
