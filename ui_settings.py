# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
    QDialog, QDialogButtonBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)
import fgpresources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(240, 228)
        icon = QIcon()
        iconThemeName = u"MainTheme"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/images/settingsSymbol.png", QSize(), QIcon.Normal, QIcon.Off)
        
        Dialog.setWindowIcon(icon)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 221, 171))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.themeComboBox = QComboBox(self.layoutWidget)
        self.themeComboBox.setObjectName(u"themeComboBox")

        self.gridLayout.addWidget(self.themeComboBox, 1, 0, 1, 2)

        self.openThemeButton = QPushButton(self.layoutWidget)
        self.openThemeButton.setObjectName(u"openThemeButton")
        font = QFont()
        font.setPointSize(9)
        self.openThemeButton.setFont(font)

        self.gridLayout.addWidget(self.openThemeButton, 2, 0, 1, 1)

        self.refreshButton = QPushButton(self.layoutWidget)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setFont(font)
        self.refreshButton.setFlat(False)

        self.gridLayout.addWidget(self.refreshButton, 2, 1, 1, 1)

        self.useWhiteButtonsOption = QCheckBox(self.layoutWidget)
        self.useWhiteButtonsOption.setObjectName(u"useWhiteButtonsOption")

        self.gridLayout.addWidget(self.useWhiteButtonsOption, 3, 0, 1, 2)

        self.checkForUpdatesBox = QCheckBox(self.layoutWidget)
        self.checkForUpdatesBox.setObjectName(u"checkForUpdatesBox")

        self.gridLayout.addWidget(self.checkForUpdatesBox, 4, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Application Theme", None))
        self.openThemeButton.setText(QCoreApplication.translate("Dialog", u"Open Theme Folder", None))
#if QT_CONFIG(tooltip)
        self.refreshButton.setToolTip(QCoreApplication.translate("Dialog", u"Refreshes themes.json", None))
#endif // QT_CONFIG(tooltip)
        self.refreshButton.setText(QCoreApplication.translate("Dialog", u"Refresh Themes", None))
        self.useWhiteButtonsOption.setText(QCoreApplication.translate("Dialog", u"Use White Buttons", None))
        self.checkForUpdatesBox.setText(QCoreApplication.translate("Dialog", u"Check for Updates at Startup", None))
    # retranslateUi

