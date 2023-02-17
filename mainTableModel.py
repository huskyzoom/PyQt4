# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore, uic
import sys
import pandas as pd
import numpy as np




class mainTableModel(QtCore.QAbstractTableModel):
    
    def __init__(self, datas, parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__datas = datas #private list __colors stores the incoming data
        
    def flags(self, index): # check if data is editable
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

# every model has to implement two methods: data and rowCount
    
    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section< self.__datas.columns.size:
                    return self.__datas.columns[section]
                else:
                    return "not implemented"
            else:
                if section<len(self.__datas.values):
                    return self.__datas.index[section]
                else:
                    return "TEMP"
        else:
            return None


    def rowCount(self, parent): # data is in 1-D so don't need to consider the parent
        return len(self.__datas.values) # show exactly the number of the rows
    
    def columnCount(self, parent):
        return self.__datas.columns.size
    
    def data(self, index, role):
            
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            value = str(self.__datas.iloc[row,column])
            return value
    
        if role == QtCore.Qt.ToolTipRole: # returns tooltip
            row = index.row()
            column = index.column()
            return " Value: " + str(self.__datas.iloc[row,column])
        
        if role == QtCore.Qt.DisplayRole: #DisplayRole: returns str to display
            
            row = index.row()
            column = index.column()
            value = str(self.__datas.iloc[row,column])
            
            return value

    def setData(self, index, value, role = QtCore.Qt.EditRole): 
        # receive the value in the View after we edited 
        if role == QtCore.Qt.EditRole:
            
            row = index.row()
            column = index.column()
          
            self.__datas.iloc[row,column] = value
            self.dataChanged.emit(index, index) #index & index: top left to bottom
        return False


    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)
        
        for i in range(rows):
            defaultValues = ["default" for i in range(self.columnCount(None))]
            
            self.__datas.insert(position, defaultValues)
        
        self.endInsertRows()
        
        return True
    
    def insertColumns(self, position, columns, parent=QtCore.QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns -1)
        
        rowCount = len(self.__datas.values)
        defaultValues = "CC"
        for i in range(columns):
            for j in range(rowCount):
                self.__datas.iloc[j].insert(position, defaultValues)
        self.endInsertColumns()
        return True
    
    
    def removeRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows - 1)

        for i in range(rows):
            value = self.__datas[position]
            self.__datas.remove(value)
             

        self.endRemoveRows()
        return True
    
    def removeColumns(self, position, columns, parent=QtCore.QModelIndex()):
        self.beginRemoveColumns(parent, position, position +columns -1)
        
        for i in range(columns):
            rowCount= len(self.__datas.values)
            for j in range(rowCount):
                value = self.__datas.iloc[j][position]
                self.__datas.remove(value)
            
        self.endRemoveColumns()
        return True
    
    def setColumnCount(self, number):
        self.totalColumn=number
        self.reset()



if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    app.setStyle("plastique")

    #ALL OF OUR VIEWS
    #comboBox = QtGui.QComboBox()
    #comboBox.show()

    tableView = QtGui.QTableView()
    tableView.show()
    
 
   
# plain Table as DataFrame
    df0 = pd.DataFrame(np.random.randint(low=1, high=10, size=(5, 5)), columns=['a','d','c','s','f'],index=['A','B','C','D','E'])
    

    print(df0)
    
    print(df0.values, type(df0.values))
    
    model = mainTableModel(df0)
    print(df0.index, df0.columns)
    print(df0.iloc[:,1], type(df0.iloc[:,1]))



   # Create the model now: one parameter is a list

    #model.insertRows(0, 1)
    #model.insertColumns(2,2)
    #model.removeRows(2,2)
    #model.setColumnCount(2)

    #comboBox.setModel(model)
    tableView.setModel(model)
    
    
    app.exec_()