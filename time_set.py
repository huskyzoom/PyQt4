# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeset.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
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

class Ui_Dialog_set_time(QtGui.QDialog):
    
    def __init__(self, parent=None):
        super(Ui_Dialog_set_time, self).__init__(parent)
        print((__name__)) 

        #Dialog_set_time = QtGui.QDialog()
        self.setObjectName(_fromUtf8("Dialog_set_time"))
        self.resize(547, 218)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.time_label = QtGui.QLabel(self)
        self.time_label.setMinimumSize(QtCore.QSize(141, 31))
        self.time_label.setMaximumSize(QtCore.QSize(141, 31))
        self.time_label.setObjectName(_fromUtf8("time_label"))
        self.verticalLayout.addWidget(self.time_label)
        self.dateEdit_2 = QtGui.QDateEdit(self)
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 4, 25), QtCore.QTime(16, 28, 0)))
        self.dateEdit_2.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.verticalLayout.addWidget(self.dateEdit_2)
        self.time_label_2 = QtGui.QLabel(self)
        self.time_label_2.setMinimumSize(QtCore.QSize(141, 31))
        self.time_label_2.setMaximumSize(QtCore.QSize(141, 31))
        self.time_label_2.setObjectName(_fromUtf8("time_label_2"))
        self.verticalLayout.addWidget(self.time_label_2)
        self.dateEdit = QtGui.QDateEdit(self)
        self.dateEdit.setWrapping(False)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 4, 26), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.verticalLayout.addWidget(self.dateEdit)
        
        
        self.buttonBox_time = QtGui.QDialogButtonBox(self)
        self.buttonBox_time.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_time.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_time.setObjectName(_fromUtf8("buttonBox_time"))
        self.verticalLayout.addWidget(self.buttonBox_time)

        self.retranslateUi()
        
        self.buttonBox_time.accepted.connect(self.accept)
        self.buttonBox_time.rejected.connect(self.reject)
        '''+
        QtCore.QObject.connect(self.buttonBox_time, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.buttonBox_time, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        '''
    def format1(self):
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 4, 25), QtCore.QTime(16, 28, 0)))
        
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 4, 26), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setDisplayFormat("yyyy/mm/dd")
        self.dateEdit_2.setDisplayFormat("yyyy/mm/dd") 
        
    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog_set_time", "Time Setting", None))
        self.time_label.setText(_translate("Dialog_set_time", "import data from", None))
        self.time_label_2.setText(_translate("Dialog_set_time", "to", None))
        
    
    def returndate(self):
        print(type(self.dateEdit_2.date()))
        print(type(self.dateEdit.date()))
        print(self.dateEdit_2.date(), self.dateEdit.date())
        return (self.dateEdit_2.date(), self.dateEdit.date())
    
    def getdate(perent=None):
        
        #dialog = Ui_Dialog_set_time(self)
        
        dlg = Ui_Dialog_set_time()
        dlg.exec_()
        twodates = dlg.returndate()
        print(twodates, dlg.result())
        return twodates
        
        
        
        '''
        dlg = Ui_Dialog_set_time()
        result = dlg.exec_()
        #result == QtGui.QDialog.Accepted
        twodates = dlg.returndate()
        
        if result == dlg.Accepted:
            print('accept', dlg.result())
            return twodates
            
        else:
            print('reject', dlg.result())
            return (QtCore.QDate(2017, 12, 1),QtCore.QDate(2017, 12, 2))
        '''

            #return (self.dateEdit_2.minimumDate(), self.dateEdit_2.maximumDate())

        
if __name__ == "__main__":
    
    
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Dialog_set_time()
    
    #ui.setupUi(Dialog_set_time)
    #Dialog_set_time.show()
    
    date, date_1 = ui.getdate()
    print("{} {}".format(date, date_1))
    sys.exit(app.exec_())
        
        
