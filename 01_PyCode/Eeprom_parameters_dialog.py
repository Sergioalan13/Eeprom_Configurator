# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Eeprom_parameters_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.AcceptRejectButtonBox = QDialogButtonBox(Dialog)
        self.AcceptRejectButtonBox.setObjectName(u"AcceptRejectButtonBox")
        self.AcceptRejectButtonBox.setGeometry(QRect(30, 240, 341, 32))
        self.AcceptRejectButtonBox.setOrientation(Qt.Horizontal)
        self.AcceptRejectButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.EepromParametersName = QLabel(Dialog)
        self.EepromParametersName.setObjectName(u"EepromParametersName")
        self.EepromParametersName.setGeometry(QRect(10, 10, 251, 31))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.EepromParametersName.setFont(font)
        self.EepromNameText = QLabel(Dialog)
        self.EepromNameText.setObjectName(u"EepromNameText")
        self.EepromNameText.setGeometry(QRect(50, 80, 47, 13))
        font1 = QFont()
        font1.setPointSize(12)
        self.EepromNameText.setFont(font1)
        self.EepromSizeText = QLabel(Dialog)
        self.EepromSizeText.setObjectName(u"EepromSizeText")
        self.EepromSizeText.setGeometry(QRect(50, 130, 101, 21))
        self.EepromSizeText.setFont(font1)
        self.EepromNameLineTextEdit = QLineEdit(Dialog)
        self.EepromNameLineTextEdit.setObjectName(u"EepromNameLineTextEdit")
        self.EepromNameLineTextEdit.setGeometry(QRect(120, 70, 221, 31))
        self.EepromNameLineTextEdit.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.EepromSizeComboBox = QComboBox(Dialog)
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.setObjectName(u"EepromSizeComboBox")
        self.EepromSizeComboBox.setGeometry(QRect(120, 130, 221, 21))
        self.EepromSizeComboBox.setFont(font1)
        self.EepromSizeComboBox.setLayoutDirection(Qt.LeftToRight)

        self.retranslateUi(Dialog)
        self.AcceptRejectButtonBox.accepted.connect(Dialog.accept)
        self.AcceptRejectButtonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Eeprom parameters configuration", None))
        self.EepromParametersName.setText(QCoreApplication.translate("Dialog", u"Eeprom parameters", None))
        self.EepromNameText.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.EepromSizeText.setText(QCoreApplication.translate("Dialog", u"Size:", None))
        self.EepromSizeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"1 kBit", None))
        self.EepromSizeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"2 Kbit", None))
        self.EepromSizeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"4 Kbit", None))
        self.EepromSizeComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"8 Kbit", None))
        self.EepromSizeComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"16 Kbit", None))
        self.EepromSizeComboBox.setItemText(5, QCoreApplication.translate("Dialog", u"32 Kbit", None))
        self.EepromSizeComboBox.setItemText(6, QCoreApplication.translate("Dialog", u"64 Kbit", None))
        self.EepromSizeComboBox.setItemText(7, QCoreApplication.translate("Dialog", u"128 Kbit", None))
        self.EepromSizeComboBox.setItemText(8, QCoreApplication.translate("Dialog", u"256 kBit", None))
        self.EepromSizeComboBox.setItemText(9, QCoreApplication.translate("Dialog", u"512 Kbit", None))
        self.EepromSizeComboBox.setItemText(10, QCoreApplication.translate("Dialog", u"1024 kBit", None))

    # retranslateUi

