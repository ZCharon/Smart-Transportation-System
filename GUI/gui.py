# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1590, 915)
        Dialog.setStyleSheet("")
        self.label_head = QtWidgets.QLabel(Dialog)
        self.label_head.setGeometry(QtCore.QRect(430, 0, 491, 31))
        self.label_head.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"\n"
"")
        self.label_head.setAlignment(QtCore.Qt.AlignCenter)
        self.label_head.setObjectName("label_head")
        self.label_frame = QtWidgets.QLabel(Dialog)
        self.label_frame.setEnabled(True)
        self.label_frame.setGeometry(QtCore.QRect(10, 30, 1331, 821))
        self.label_frame.setMouseTracking(True)
        self.label_frame.setStyleSheet("background-color:black\n"
"")
        self.label_frame.setObjectName("label_frame")
        self.label_mouse_x = QtWidgets.QLabel(Dialog)
        self.label_mouse_x.setGeometry(QtCore.QRect(1190, 860, 72, 15))
        self.label_mouse_x.setStyleSheet("")
        self.label_mouse_x.setText("")
        self.label_mouse_x.setObjectName("label_mouse_x")
        self.label_mouse_y = QtWidgets.QLabel(Dialog)
        self.label_mouse_y.setGeometry(QtCore.QRect(1270, 860, 72, 15))
        self.label_mouse_y.setStyleSheet("")
        self.label_mouse_y.setText("")
        self.label_mouse_y.setObjectName("label_mouse_y")
        self.label_up_count = QtWidgets.QLabel(Dialog)
        self.label_up_count.setGeometry(QtCore.QRect(1410, 270, 61, 16))
        self.label_up_count.setStyleSheet("")
        self.label_up_count.setText("")
        self.label_up_count.setObjectName("label_up_count")
        self.label_down_count = QtWidgets.QLabel(Dialog)
        self.label_down_count.setGeometry(QtCore.QRect(1350, 270, 61, 16))
        self.label_down_count.setStyleSheet("")
        self.label_down_count.setText("")
        self.label_down_count.setObjectName("label_down_count")
        self.label_traffic_detail = QtWidgets.QLabel(Dialog)
        self.label_traffic_detail.setGeometry(QtCore.QRect(1350, 250, 141, 16))
        self.label_traffic_detail.setStyleSheet("")
        self.label_traffic_detail.setText("")
        self.label_traffic_detail.setObjectName("label_traffic_detail")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1460, 20, 111, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_illegal_parking = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_illegal_parking.setObjectName("btn_illegal_parking")
        self.verticalLayout.addWidget(self.btn_illegal_parking)
        self.btn_retrograde = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_retrograde.setObjectName("btn_retrograde")
        self.verticalLayout.addWidget(self.btn_retrograde)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1360, 20, 101, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_open_video = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_open_video.setStyleSheet("")
        self.btn_open_video.setObjectName("btn_open_video")
        self.verticalLayout_2.addWidget(self.btn_open_video)
        self.btn_go_detect = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_go_detect.setObjectName("btn_go_detect")
        self.verticalLayout_2.addWidget(self.btn_go_detect)
        self.btn_stop_detect = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_stop_detect.setObjectName("btn_stop_detect")
        self.verticalLayout_2.addWidget(self.btn_stop_detect)
        self.label_ill_parking = QtWidgets.QLabel(Dialog)
        self.label_ill_parking.setGeometry(QtCore.QRect(1350, 300, 221, 151))
        self.label_ill_parking.setText("")
        self.label_ill_parking.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_ill_parking.setObjectName("label_ill_parking")
        self.combox_fun = QtWidgets.QComboBox(Dialog)
        self.combox_fun.setGeometry(QtCore.QRect(1470, 0, 120, 21))
        self.combox_fun.setObjectName("combox_fun")
        self.combox_fun.addItem("")
        self.combox_fun.addItem("")
        self.combox_fun.addItem("")
        self.label_line1 = QtWidgets.QLabel(Dialog)
        self.label_line1.setGeometry(QtCore.QRect(1350, 460, 221, 16))
        self.label_line1.setText("")
        self.label_line1.setObjectName("label_line1")
        self.label_line0 = QtWidgets.QLabel(Dialog)
        self.label_line0.setGeometry(QtCore.QRect(1350, 280, 231, 16))
        self.label_line0.setText("")
        self.label_line0.setObjectName("label_line0")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_head.setText(_translate("Dialog", "请选择视频进行分析"))
        self.label_frame.setText(_translate("Dialog", "请选择视频分析"))
        self.btn_illegal_parking.setText(_translate("Dialog", "违停检测"))
        self.btn_retrograde.setText(_translate("Dialog", "逆行检测"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.btn_open_video.setText(_translate("Dialog", "打开视频"))
        self.btn_go_detect.setText(_translate("Dialog", "开始检测"))
        self.btn_stop_detect.setText(_translate("Dialog", "暂停播放"))
        self.combox_fun.setItemText(0, _translate("Dialog", "功能"))
        self.combox_fun.setItemText(1, _translate("Dialog", "清空车流量"))
        self.combox_fun.setItemText(2, _translate("Dialog", "清空违停统计"))
