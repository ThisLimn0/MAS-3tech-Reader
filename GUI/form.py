# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(849, 533)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ExcelBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ExcelBox.setGeometry(QtCore.QRect(40, 270, 121, 26))
        self.ExcelBox.setObjectName("ExcelBox")
        self.PDFBox = QtWidgets.QCheckBox(self.centralwidget)
        self.PDFBox.setGeometry(QtCore.QRect(40, 300, 101, 26))
        self.PDFBox.setObjectName("PDFBox")
        self.RemoveButton = QtWidgets.QRadioButton(self.centralwidget)
        self.RemoveButton.setGeometry(QtCore.QRect(40, 190, 301, 21))
        self.RemoveButton.setObjectName("RemoveButton")
        self.CopyButton = QtWidgets.QRadioButton(self.centralwidget)
        self.CopyButton.setGeometry(QtCore.QRect(40, 220, 112, 26))
        self.CopyButton.setObjectName("CopyButton")
        self.IndexButton = QtWidgets.QRadioButton(self.centralwidget)
        self.IndexButton.setGeometry(QtCore.QRect(40, 160, 131, 26))
        self.IndexButton.setObjectName("IndexButton")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(350, 190, 461, 281))
        self.treeWidget.setObjectName("treeWidget")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(30, 380, 171, 71))
        self.StartButton.setObjectName("StartButton")
        self.PathBox = QtWidgets.QTextEdit(self.centralwidget)
        self.PathBox.setGeometry(QtCore.QRect(40, 40, 691, 41))
        self.PathBox.setObjectName("PathBox")
        self.PrintBox = QtWidgets.QCheckBox(self.centralwidget)
        self.PrintBox.setGeometry(QtCore.QRect(220, 400, 61, 26))
        self.PrintBox.setObjectName("PrintBox")
        self.OutputBox = QtWidgets.QTextEdit(self.centralwidget)
        self.OutputBox.setGeometry(QtCore.QRect(40, 90, 691, 41))
        self.OutputBox.setObjectName("OutputBox")
        self.PDFLineBox = QtWidgets.QTextEdit(self.centralwidget)
        self.PDFLineBox.setGeometry(QtCore.QRect(120, 300, 51, 31))
        self.PDFLineBox.setAutoFillBackground(True)
        self.PDFLineBox.setObjectName("PDFLineBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 307, 47, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 21))
        self.menubar.setObjectName("menubar")
        self.menuMAS_Reader = QtWidgets.QMenu(self.menubar)
        self.menuMAS_Reader.setObjectName("menuMAS_Reader")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDatei = QtWidgets.QAction(MainWindow)
        self.actionDatei.setObjectName("actionDatei")
        self.menubar.addAction(self.menuMAS_Reader.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ExcelBox.setText(_translate("MainWindow", "Excel Export"))
        self.PDFBox.setText(_translate("MainWindow", "PDF Export"))
        self.RemoveButton.setText(_translate("MainWindow", "Verschieben (Doppelte Überschreiben)"))
        self.CopyButton.setText(_translate("MainWindow", "Kopieren"))
        self.IndexButton.setText(_translate("MainWindow", "Nur Indizieren"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Aufstellorte"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Rechnungen"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.PathBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:12pt;\">Input</span></p></body></html>"))
        self.PrintBox.setText(_translate("MainWindow", "Print"))
        self.OutputBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:12pt;\">Output</span></p></body></html>"))
        self.PDFLineBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:12pt;\">100</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Zeilen</span></p></body></html>"))
        self.menuMAS_Reader.setTitle(_translate("MainWindow", "MAS Reader"))
        self.actionDatei.setText(_translate("MainWindow", "Datei"))
