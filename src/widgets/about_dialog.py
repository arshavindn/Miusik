# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Cloud/Dropbox/Programming/Code/py/Miusik/src/ui/about_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 350)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 350))
        Dialog.setMaximumSize(QtCore.QSize(400, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/miusik.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(90, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(150, 150))
        self.label.setMaximumSize(QtCore.QSize(150, 150))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/miusik.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(90, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setText(_fromUtf8("Miusik 0.1 Beta"))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 25))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setText(_fromUtf8("<a href=\"https://github.com/arshavindn/Miusik\">https://github.com/arshavindn/Miusik</a>"))
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About", None))
        self.label_3.setText(_translate("Dialog", "Developers:", None))
        self.label_4.setText(_translate("Dialog", "Trần Viết Hà", None))
        self.label_5.setText(_translate("Dialog", "Lưu Đinh Hải Châu", None))
        self.label_6.setText(_translate("Dialog", "Lê Xuân Diệu", None))
        self.label_7.setText(_translate("Dialog", "Bùi Văn Thanh Khuê", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
