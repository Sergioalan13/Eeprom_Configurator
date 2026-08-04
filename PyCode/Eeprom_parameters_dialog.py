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

class Ui_EepromParameters(object):
    def setupUi(self, EepromParameters):
        if not EepromParameters.objectName():
            EepromParameters.setObjectName(u"EepromParameters")
        EepromParameters.resize(400, 451)
        self.AcceptRejectButtonBox = QDialogButtonBox(EepromParameters)
        self.AcceptRejectButtonBox.setObjectName(u"AcceptRejectButtonBox")
        self.AcceptRejectButtonBox.setGeometry(QRect(50, 390, 291, 32))
        self.AcceptRejectButtonBox.setOrientation(Qt.Horizontal)
        self.AcceptRejectButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.EepromParametersName = QLabel(EepromParameters)
        self.EepromParametersName.setObjectName(u"EepromParametersName")
        self.EepromParametersName.setGeometry(QRect(10, 10, 251, 31))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.EepromParametersName.setFont(font)
        self.EepromNameText = QLabel(EepromParameters)
        self.EepromNameText.setObjectName(u"EepromNameText")
        self.EepromNameText.setGeometry(QRect(50, 90, 51, 16))
        font1 = QFont()
        font1.setPointSize(12)
        self.EepromNameText.setFont(font1)
        self.EepromSizeText = QLabel(EepromParameters)
        self.EepromSizeText.setObjectName(u"EepromSizeText")
        self.EepromSizeText.setGeometry(QRect(50, 140, 51, 21))
        self.EepromSizeText.setFont(font1)
        self.EepromNameLineTextEdit = QLineEdit(EepromParameters)
        self.EepromNameLineTextEdit.setObjectName(u"EepromNameLineTextEdit")
        self.EepromNameLineTextEdit.setGeometry(QRect(170, 80, 171, 31))
        self.EepromNameLineTextEdit.setFont(font1)
        self.EepromNameLineTextEdit.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.EepromSizeComboBox = QComboBox(EepromParameters)
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.addItem("")
        self.EepromSizeComboBox.setObjectName(u"EepromSizeComboBox")
        self.EepromSizeComboBox.setGeometry(QRect(170, 130, 171, 31))
        self.EepromSizeComboBox.setFont(font1)
        self.EepromSizeComboBox.setLayoutDirection(Qt.LeftToRight)
        self.EepromStartAddressText = QLabel(EepromParameters)
        self.EepromStartAddressText.setObjectName(u"EepromStartAddressText")
        self.EepromStartAddressText.setGeometry(QRect(50, 190, 111, 21))
        self.EepromStartAddressText.setFont(font1)
        self.EepromNoPagesText = QLabel(EepromParameters)
        self.EepromNoPagesText.setObjectName(u"EepromNoPagesText")
        self.EepromNoPagesText.setGeometry(QRect(50, 240, 81, 21))
        self.EepromNoPagesText.setFont(font1)
        self.EepromPageSizeText = QLabel(EepromParameters)
        self.EepromPageSizeText.setObjectName(u"EepromPageSizeText")
        self.EepromPageSizeText.setGeometry(QRect(50, 290, 81, 21))
        self.EepromPageSizeText.setFont(font1)
        self.EepromStartAddressLineTextEdit = QLineEdit(EepromParameters)
        self.EepromStartAddressLineTextEdit.setObjectName(u"EepromStartAddressLineTextEdit")
        self.EepromStartAddressLineTextEdit.setGeometry(QRect(170, 180, 171, 31))
        self.EepromStartAddressLineTextEdit.setFont(font1)
        self.EepromNoPagesLineTextEdit = QLineEdit(EepromParameters)
        self.EepromNoPagesLineTextEdit.setObjectName(u"EepromNoPagesLineTextEdit")
        self.EepromNoPagesLineTextEdit.setGeometry(QRect(170, 230, 171, 31))
        self.EepromNoPagesLineTextEdit.setFont(font1)
        self.EepromPageSizeLineTextEdit = QLineEdit(EepromParameters)
        self.EepromPageSizeLineTextEdit.setObjectName(u"EepromPageSizeLineTextEdit")
        self.EepromPageSizeLineTextEdit.setGeometry(QRect(170, 280, 171, 31))
        self.EepromPageSizeLineTextEdit.setFont(font1)
        self.EepromI2cAddressText = QLabel(EepromParameters)
        self.EepromI2cAddressText.setObjectName(u"EepromI2cAddressText")
        self.EepromI2cAddressText.setGeometry(QRect(50, 340, 101, 21))
        self.EepromI2cAddressText.setFont(font1)
        self.EepromI2cAddressLineTextEdit = QLineEdit(EepromParameters)
        self.EepromI2cAddressLineTextEdit.setObjectName(u"EepromI2cAddressLineTextEdit")
        self.EepromI2cAddressLineTextEdit.setGeometry(QRect(170, 330, 171, 31))
        self.EepromI2cAddressLineTextEdit.setFont(font1)

        self.retranslateUi(EepromParameters)
        self.AcceptRejectButtonBox.accepted.connect(EepromParameters.accept)
        self.AcceptRejectButtonBox.rejected.connect(EepromParameters.reject)

        QMetaObject.connectSlotsByName(EepromParameters)
    # setupUi

    def retranslateUi(self, EepromParameters):
        EepromParameters.setWindowTitle(QCoreApplication.translate("EepromParameters", u"Eeprom parameters configuration", None))
        self.EepromParametersName.setText(QCoreApplication.translate("EepromParameters", u"Eeprom parameters", None))
        self.EepromNameText.setText(QCoreApplication.translate("EepromParameters", u"Name:", None))
        self.EepromSizeText.setText(QCoreApplication.translate("EepromParameters", u"Size:", None))
        self.EepromNameLineTextEdit.setPlaceholderText(QCoreApplication.translate("EepromParameters", u"eeprom name", None))
        self.EepromSizeComboBox.setItemText(0, QCoreApplication.translate("EepromParameters", u"1 kBit", None))
        self.EepromSizeComboBox.setItemText(1, QCoreApplication.translate("EepromParameters", u"2 kBit", None))
        self.EepromSizeComboBox.setItemText(2, QCoreApplication.translate("EepromParameters", u"32 kBit", None))
        self.EepromSizeComboBox.setItemText(3, QCoreApplication.translate("EepromParameters", u"64 kBit", None))
        self.EepromSizeComboBox.setItemText(4, QCoreApplication.translate("EepromParameters", u"128 kBit", None))
        self.EepromSizeComboBox.setItemText(5, QCoreApplication.translate("EepromParameters", u"256 kBit", None))
        self.EepromSizeComboBox.setItemText(6, QCoreApplication.translate("EepromParameters", u"512 kBit", None))

        self.EepromStartAddressText.setText(QCoreApplication.translate("EepromParameters", u"Start Address:", None))
        self.EepromNoPagesText.setText(QCoreApplication.translate("EepromParameters", u"No. Pages:", None))
        self.EepromPageSizeText.setText(QCoreApplication.translate("EepromParameters", u"Page Size:", None))
        self.EepromStartAddressLineTextEdit.setPlaceholderText(QCoreApplication.translate("EepromParameters", u"hex", None))
        self.EepromNoPagesLineTextEdit.setPlaceholderText(QCoreApplication.translate("EepromParameters", u"dec", None))
        self.EepromPageSizeLineTextEdit.setPlaceholderText(QCoreApplication.translate("EepromParameters", u"dec", None))
        self.EepromI2cAddressText.setText(QCoreApplication.translate("EepromParameters", u"I2C Address:", None))
        self.EepromI2cAddressLineTextEdit.setPlaceholderText(QCoreApplication.translate("EepromParameters", u"hex", None))
    # retranslateUi

