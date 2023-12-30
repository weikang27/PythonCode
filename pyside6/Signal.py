from PySide6.QtCore import Signal, QObject


class MySignal(QObject):
    setResult = Signal(str)
    setProgressBar_2 = Signal(int)
    setProgressBar = Signal(int)
    setLabel_7 = Signal(str)
    setLabel_9 = Signal(str)


my_signal = MySignal()
