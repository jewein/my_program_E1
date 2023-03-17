# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.action1_2 = QAction(MainWindow)
        self.action1_2.setObjectName(u"action1_2")
        self.action1_3 = QAction(MainWindow)
        self.action1_3.setObjectName(u"action1_3")
        self.action1_4 = QAction(MainWindow)
        self.action1_4.setObjectName(u"action1_4")
        self.action1_5 = QAction(MainWindow)
        self.action1_5.setObjectName(u"action1_5")
        self.action1_6 = QAction(MainWindow)
        self.action1_6.setObjectName(u"action1_6")
        self.action1_7 = QAction(MainWindow)
        self.action1_7.setObjectName(u"action1_7")
        self.action1_8 = QAction(MainWindow)
        self.action1_8.setObjectName(u"action1_8")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action1_2)
        self.menu.addAction(self.action1_3)
        self.menu.addAction(self.action1_4)
        self.menu.addAction(self.action1_5)
        self.menu.addAction(self.action1_6)
        self.menu.addAction(self.action1_7)
        self.menu.addAction(self.action1_8)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action1_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action1_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action1_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action1_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action1_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action1_7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action1_8.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u4f60\u597d", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u662f\u5417", None))
    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())