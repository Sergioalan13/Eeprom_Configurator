# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Variable_configuration_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QLabel, QLineEdit,
    QSizePolicy, QTextEdit, QWidget)

class Ui_VariableConfiguration(object):
    def setupUi(self, VariableConfiguration):
        if not VariableConfiguration.objectName():
            VariableConfiguration.setObjectName(u"VariableConfiguration")
        VariableConfiguration.resize(402, 431)
        self.VariableAcceptRejectButton = QDialogButtonBox(VariableConfiguration)
        self.VariableAcceptRejectButton.setObjectName(u"VariableAcceptRejectButton")
        self.VariableAcceptRejectButton.setGeometry(QRect(30, 390, 341, 32))
        self.VariableAcceptRejectButton.setOrientation(Qt.Horizontal)
        self.VariableAcceptRejectButton.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.VariableParametersText = QLabel(VariableConfiguration)
        self.VariableParametersText.setObjectName(u"VariableParametersText")
        self.VariableParametersText.setGeometry(QRect(10, 10, 221, 41))
        font = QFont()
        font.setPointSize(18)
        self.VariableParametersText.setFont(font)
        self.VariableNameText = QLabel(VariableConfiguration)
        self.VariableNameText.setObjectName(u"VariableNameText")
        self.VariableNameText.setGeometry(QRect(40, 60, 61, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.VariableNameText.setFont(font1)
        self.VariableTypeText = QLabel(VariableConfiguration)
        self.VariableTypeText.setObjectName(u"VariableTypeText")
        self.VariableTypeText.setGeometry(QRect(40, 100, 61, 31))
        self.VariableTypeText.setFont(font1)
        self.VariableAddressText = QLabel(VariableConfiguration)
        self.VariableAddressText.setObjectName(u"VariableAddressText")
        self.VariableAddressText.setGeometry(QRect(40, 140, 71, 31))
        self.VariableAddressText.setFont(font1)
        self.VariableInitValueText = QLabel(VariableConfiguration)
        self.VariableInitValueText.setObjectName(u"VariableInitValueText")
        self.VariableInitValueText.setGeometry(QRect(40, 180, 71, 31))
        self.VariableInitValueText.setFont(font1)
        self.VariableCommentText = QLabel(VariableConfiguration)
        self.VariableCommentText.setObjectName(u"VariableCommentText")
        self.VariableCommentText.setGeometry(QRect(40, 220, 81, 31))
        self.VariableCommentText.setFont(font1)
        self.VariableTypeComboBox = QComboBox(VariableConfiguration)
        self.VariableTypeComboBox.addItem("")
        self.VariableTypeComboBox.addItem("")
        self.VariableTypeComboBox.addItem("")
        self.VariableTypeComboBox.addItem("")
        self.VariableTypeComboBox.addItem("")
        self.VariableTypeComboBox.addItem("")
        self.VariableTypeComboBox.addItem("")
        self.VariableTypeComboBox.setObjectName(u"VariableTypeComboBox")
        self.VariableTypeComboBox.setGeometry(QRect(120, 100, 241, 31))
        self.VariableTypeComboBox.setFont(font1)
        self.VariableName = QLineEdit(VariableConfiguration)
        self.VariableName.setObjectName(u"VariableName")
        self.VariableName.setGeometry(QRect(120, 60, 241, 31))
        self.VariableName.setFont(font1)
        self.VariableAddress = QLineEdit(VariableConfiguration)
        self.VariableAddress.setObjectName(u"VariableAddress")
        self.VariableAddress.setGeometry(QRect(120, 140, 241, 31))
        self.VariableAddress.setFont(font1)
        self.VariableInitValue = QLineEdit(VariableConfiguration)
        self.VariableInitValue.setObjectName(u"VariableInitValue")
        self.VariableInitValue.setEnabled(False)
        self.VariableInitValue.setGeometry(QRect(120, 180, 111, 31))
        self.VariableInitValue.setFont(font1)
        self.VariableInitValue.setDragEnabled(False)
        self.VariableInitValue.setReadOnly(False)
        self.VariableInitValue.setClearButtonEnabled(False)
        self.WriteVariableCheckBox = QCheckBox(VariableConfiguration)
        self.WriteVariableCheckBox.setObjectName(u"WriteVariableCheckBox")
        self.WriteVariableCheckBox.setGeometry(QRect(250, 190, 111, 17))
        font2 = QFont()
        font2.setPointSize(10)
        self.WriteVariableCheckBox.setFont(font2)
        self.WriteVariableCheckBox.setCheckable(True)
        self.WriteVariableCheckBox.setChecked(False)
        self.VariableComment = QTextEdit(VariableConfiguration)
        self.VariableComment.setObjectName(u"VariableComment")
        self.VariableComment.setGeometry(QRect(120, 220, 241, 151))
        self.VariableComment.setFont(font1)

        self.retranslateUi(VariableConfiguration)
        self.VariableAcceptRejectButton.accepted.connect(VariableConfiguration.accept)
        self.VariableAcceptRejectButton.rejected.connect(VariableConfiguration.reject)
        self.WriteVariableCheckBox.toggled.connect(self.VariableInitValue.setEnabled)

        QMetaObject.connectSlotsByName(VariableConfiguration)
    # setupUi

    def retranslateUi(self, VariableConfiguration):
        VariableConfiguration.setWindowTitle(QCoreApplication.translate("VariableConfiguration", u"Variable configuration", None))
        self.VariableParametersText.setText(QCoreApplication.translate("VariableConfiguration", u"Variable Parameters", None))
        self.VariableNameText.setText(QCoreApplication.translate("VariableConfiguration", u"Name:", None))
        self.VariableTypeText.setText(QCoreApplication.translate("VariableConfiguration", u"Type:", None))
        self.VariableAddressText.setText(QCoreApplication.translate("VariableConfiguration", u"Address:", None))
        self.VariableInitValueText.setText(QCoreApplication.translate("VariableConfiguration", u"Init value:", None))
        self.VariableCommentText.setText(QCoreApplication.translate("VariableConfiguration", u"Comment:", None))
        self.VariableTypeComboBox.setItemText(0, QCoreApplication.translate("VariableConfiguration", u"uint8_t", None))
        self.VariableTypeComboBox.setItemText(1, QCoreApplication.translate("VariableConfiguration", u"uint16_t", None))
        self.VariableTypeComboBox.setItemText(2, QCoreApplication.translate("VariableConfiguration", u"uint32_t", None))
        self.VariableTypeComboBox.setItemText(3, QCoreApplication.translate("VariableConfiguration", u"int8_t", None))
        self.VariableTypeComboBox.setItemText(4, QCoreApplication.translate("VariableConfiguration", u"int16_t", None))
        self.VariableTypeComboBox.setItemText(5, QCoreApplication.translate("VariableConfiguration", u"int32_t", None))
        self.VariableTypeComboBox.setItemText(6, QCoreApplication.translate("VariableConfiguration", u"float", None))

        self.VariableName.setPlaceholderText(QCoreApplication.translate("VariableConfiguration", u"variable name", None))
        self.VariableAddress.setPlaceholderText(QCoreApplication.translate("VariableConfiguration", u"hex", None))
        self.VariableInitValue.setPlaceholderText(QCoreApplication.translate("VariableConfiguration", u"dec", None))
        self.WriteVariableCheckBox.setText(QCoreApplication.translate("VariableConfiguration", u"Write variable", None))
        self.VariableComment.setPlaceholderText(QCoreApplication.translate("VariableConfiguration", u"optional", None))
    # retranslateUi

