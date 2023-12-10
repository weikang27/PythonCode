# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auto_wechat.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                               QMainWindow, QMenu, QMenuBar, QProgressBar,
                               QPushButton, QSizePolicy, QSpinBox, QStatusBar,
                               QTextEdit, QTimeEdit, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 542)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 10, 258, 492))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.progressBar_2 = QProgressBar(self.widget)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(0)

        self.gridLayout.addWidget(self.progressBar_2, 7, 0, 1, 4)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 6, 1, 1, 3)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.pushButton, 12, 1, 1, 3)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 11, 1, 1, 3)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 3)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 4)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 13, 0, 1, 1)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 4)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 2)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 12, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 4)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 9, 0, 1, 4)

        self.timeEdit = QTimeEdit(self.widget)
        self.timeEdit.setObjectName(u"timeEdit")

        self.gridLayout.addWidget(self.timeEdit, 6, 0, 1, 1)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999)

        self.gridLayout.addWidget(self.spinBox, 11, 0, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 13, 1, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 338, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u65f6\u65f6\u95f4", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u8bf7\u8f93\u5165\u6b64\u5185\u5bb9\u7684\u63a5\u6536\u8005\u540d\u79f0",
                                                        None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        # if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
        # endif // QT_CONFIG(shortcut)
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u53d1\u9001\u6b21\u6570", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u65f6\u95f4", None))
        self.lineEdit.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6d88\u606f\u7684\u65f6\u95f4", None))
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6b21\u6570\u8fdb\u5ea6\u6761", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u60a8\u8981\u53d1\u9001\u7684\u5185\u5bb9",
                                       None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm:ss", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u53d1\u9001", None))
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u5012\u8ba1\u65f6\u8fdb\u5ea6\u6761", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi
