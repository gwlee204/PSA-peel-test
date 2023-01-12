# MIT License

# Copyright (c) 2023 Geon-woo Lee

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'peel.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ui_datapath = QtWidgets.QLineEdit(self.centralwidget)
        self.ui_datapath.setReadOnly(True)
        self.ui_datapath.setObjectName("ui_datapath")
        self.horizontalLayout.addWidget(self.ui_datapath)
        self.ui_datapath_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ui_datapath_btn.setObjectName("ui_datapath_btn")
        self.horizontalLayout.addWidget(self.ui_datapath_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.ui_filelist = QtWidgets.QListWidget(self.centralwidget)
        self.ui_filelist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui_filelist.setObjectName("ui_filelist")
        self.verticalLayout_2.addWidget(self.ui_filelist)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.ui_datatable = QtWidgets.QTableWidget(self.centralwidget)
        self.ui_datatable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui_datatable.setObjectName("ui_datatable")
        self.ui_datatable.setColumnCount(0)
        self.ui_datatable.setRowCount(0)
        self.verticalLayout_2.addWidget(self.ui_datatable)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(4, 2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ui_graph = PlotWidget(self.centralwidget)
        self.ui_graph.setObjectName("ui_graph")
        self.verticalLayout.addWidget(self.ui_graph)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ui_average = QtWidgets.QLineEdit(self.centralwidget)
        self.ui_average.setReadOnly(True)
        self.ui_average.setObjectName("ui_average")
        self.gridLayout.addWidget(self.ui_average, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ui_stdev = QtWidgets.QLineEdit(self.centralwidget)
        self.ui_stdev.setReadOnly(True)
        self.ui_stdev.setObjectName("ui_stdev")
        self.gridLayout.addWidget(self.ui_stdev, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.ui_save = QtWidgets.QPushButton(self.centralwidget)
        self.ui_save.setObjectName("ui_save")
        self.verticalLayout.addWidget(self.ui_save)
        self.verticalLayout.setStretch(0, 1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PSA Peel Strength Analyzer"))
        self.ui_datapath_btn.setText(_translate("MainWindow", "Set data path"))
        self.label_6.setText(_translate("MainWindow", "File list"))
        self.label_5.setText(_translate("MainWindow", "Raw data"))
        self.label.setText(_translate("MainWindow", "Average Peel Strength"))
        self.label_3.setText(_translate("MainWindow", "N/25mm"))
        self.label_2.setText(_translate("MainWindow", "Standard deviation"))
        self.label_4.setText(_translate("MainWindow", "N/25mm"))
        self.ui_save.setText(_translate("MainWindow", "Save all results"))