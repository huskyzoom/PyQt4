# -*- coding: utf-8 -*-
__appname__ = "MA"
__module__ = "main"

import logging #allows us to log the output of our application like printing to a file. For code hunting
import importlib
importlib.reload(logging)
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#import plot1

import sqlite3 # save a database as a file
import re # regular expression module in python
import os #use a method from OS module to determine the path of the application data
import csv
import traceback # traceback while debugging 
# IMPORT classes
import plot1
from mplwidget import *
import MA_UII
import mainTableModel
import embed_in_qt4_navbar
from time_set import *
from date_dialog import *

import time
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import CoolProp.CoolProp as CP
from CoolProp.CoolProp import PropsSI




'''
# set up path of AppData using OS
appDataPath = os.environ["APPDATA"] + "\\pyMA\\" #create the own folder "DataMan"
if not os.path.exists(appDataPath): 
    try:
        os.makedirs(appDataPath)
    except Exception as e: # in Python3, use "Exception as e", instead "Exception, e"
        appDataPath = os.getcwd() #getcwd() returns the current working directory, which is for me: User\\Yuqian
        
# To define logging:
print(logging.__version__)
logging.basicConfig(filename = appDataPath + "pyMA.log",
                    format = "%(asctime)-15s: %(name)-18s - %(levelname)-8s - %(module)-15s - %(funcName)-20s - %(lineno)-6d - %(message)s",
                    level =logging.DEBUG) #where to save log files
logger = logging.getLogger(name = "main-gui")       
'''  

'''
class secondUI(object):
    def setupUi(self):
        a = self.listWidget.selectedItems()
        Title = a[len(a)-1].text()
        self.setWindowTitle(Title)
        
'''
# MAIN CLASS

class Main(QMainWindow, MA_UII.Ui_MainWindow, ):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.mouseDoubleClickEvent
        
        self.Widget = self.stackedWidget.findChildren(QWidget)
        self.Widget1 = self.findChild((QtGui.QWidget, ), '')
        self.Widget2 = self.findChild((QtGui.QWidget, ), '')
#        print(self.Widget1)
        sender = self.sender()
#        print(sender)  
        self.Widget1.installEventFilter(self)
        self.Widget2.installEventFilter(self)
#        self.DoubleClicked.connect(self.eventFilter)
    # connect actions
        self.actionImport.triggered.connect(self.import_action_triggered)
        self.actionExport.triggered.connect(self.export_action_triggered)
        self.actionClose.triggered.connect(self.exit_action_triggered)
        #plot Agilent or Strom or Wetter
#        self.mouseDoubleClickEvent.connect(self.)
        self.boxDiagramBtnPlot_AG.clicked.connect(self.plotCSV)
        self.boxDiagramBtnPlot_AG.clicked.connect(self.plot1)
        self.boxDiagramBtnPlot_Strom.clicked.connect(self.plotCSV_s)
        self.boxDiagramBtnPlot_Strom.clicked.connect(self.plot2)
        self.boxDiagramBtnPlot_Wetter.clicked.connect(self.plotCSV_w)
        self.boxDiagramBtnPlot_Wetter.clicked.connect(self.plot3)
        
        self.boxDiagramBtnNW_AG.clicked.connect(self.plotCSVnewWindow)
        self.tab1Med_Btn_apply.clicked.connect(self.tab1Med_apply)
        self.boxTableBtnCalc_AG.clicked.connect(self.calculateQ)
        #self.listWidget.itemDoubleClicked.connect(self.showMaximized)
        self.listWidget.itemDoubleClicked.connect(self.change_page)
        #self.tab1Med_combo_HCir.activated[str].connect(self.tab1Med_label)
    
        self.load_initial_settings()
    
        
        self.actionClose.triggered.connect(self.exit_action_triggered)
        
#    def save1(self):
##        if self.plotCSV:
##            
##            
##        self.Strom_tab2mpl.canvas.save('aaa.png')
#        plot1.MplCanvas(self).draw()
#        self.fuck = plot1.ApplicationWindow()
#        self.fuck.show()
        
    def eventFilter(self, obj, event):
        if obj == self.Widget2: 
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
#                mouseEvent = QMouseEvent(event)     
                print('aaa')
        return  QMainWindow.eventFilter(self, obj, event) 
        
    def change_page(self):
        page = self.listWidget.currentRow()

        if page == 0:
            self.stackedWidget.setCurrentIndex(0)
            self.stackedWidget_List.setCurrentIndex(0)
        elif page == 1:
            self.stackedWidget.setCurrentIndex(1)
            self.stackedWidget_List.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(2)
            self.stackedWidget_List.setCurrentIndex(2)
        


    def load_initial_settings(self):
        # print("10")
         
    def export_action_triggered(self):
        date = time_set.Ui_Dialog_set_time.getdate()
        # print(date[0])
        
    def exit_action_triggered(self):
        self.close()
        
#    def changeformat(self):
#            start_date_a, end_date_a = time_dlg_a.returndate()
#    
#            start_a = QDate.toString(start_date_a, 'dd.MM.yyyy')
#            end_a = QDate.toString(end_date_a, 'dd.MM.yyyy')
#        if "Strom" in self.dbFile:
#            self.datetime.setDisplayFormat('yyyy.MM.dd')
#        else :
#            self.datetime.setDisplayFormat('dd.MM.yyyy')   

        
    def import_action_triggered(self):
        dbFile = QFileDialog.getOpenFileName(self, caption="Import data",
                                             directory=".", filter="CSV File (*.csv)")

        print(dbFile)
#        self.changeformat()
        
        if dbFile:
#            try:

    # Update Calc List:
            Agil_list = []
        
            self.filename = ""
            if "" in dbFile:
                self.filename = ""
                time_dlg_a = Ui_Dialog_set_time()
                time_dlg_a.exec_()
                start_date_a, end_date_a = time_dlg_a.returndate()

                start_a = QDate.toString(start_date_a, 'dd.MM.yyyy')
                end_a = QDate.toString(end_date_a, 'dd.MM.yyyy')
                print(start_a, end_a, time_dlg_a.result(), '121')
                
                
                
                if time_dlg_a.result():
                    self.boxTableLabel_AG.setText(self.filename)
                    self.boxTableListWidget_AG.clear()
                    self.boxTableListWidget_AG.addItems(Agil_list)
                    self.boxDiagramListWidget_AG.clear()
                    self.csv2pd = pd.read_csv(dbFile, engine='python', decimal=',', sep=';' ,encoding="utf-16", 
                                        skiprows=4,  header =0)
            # Split datetime to date and time:
                    self.csv2pd[''], self.csv2pd[''] = self.csv2pd[''].str.split('\s',1).str[1],self.csv2pd[''].str.split('\s',1).str[0]

                    self.csv2pd.set_index('',inplace=True)

                    self.csv2pd = self.csv2pd.ix[start_a:end_a]

                
                else:
                    self.boxTableLabel_AG.setText(self.filename)
                    self.boxTableListWidget_AG.clear()
                    self.boxTableListWidget_AG.addItems(Agil_list)
                    self.boxDiagramListWidget_AG.clear()                
                    self.csv2pd = pd.read_csv(dbFile, engine='python', decimal=',', sep=';' ,encoding="utf-16", 
                                        skiprows=4, header =0)
                    self.csv2pd[''], self.csv2pd['d'] = self.csv2pd[''].str.split('\s',1).str[1],self.csv2pd[''].str.split('\s',1).str[0]
                
                    self.csv2pd.set_index('d',inplace=True)

                for column in self.csv2pd.columns:
                    self.boxDiagramListWidget_AG.addItem(column)
        
        # Whole Dataset as Model1
                self.model1 = mainTableModel.mainTableModel(self.csv2pd)
                self.AG_tab2TableView.setModel(self.model1)            
            #timeit.timeit(self.calculateQ)
            
        # Status bar
                self.mainStatusbar.showMessage("Import\t" + str(dbFile))
                QMessageBox.information(self, __appname__, "Successfully imported\n " + str(self.csv2pd.shape) + " table" )

            elif "" in dbFile:
                self.filename = ""
        # set up time period:
                
                time_dlg = Ui_Dialog_set_time()
                time_dlg.format1()
                time_dlg.exec_()
                
                
                start_date_s, end_date_s = time_dlg.returndate()

                start_s = QDate.toString(start_date_s, 'dd.MM.yyyy')
                end_s = QDate.toString(end_date_s, 'dd.MM.yyyy')#'yyyy.MM.dd'
                print(start_s, end_s, time_dlg.result())
                
                if time_dlg.result():
                    self.boxTableLabel_Strom.setText(self.filename)
                    self.boxDiagramListWidget_Strom.clear()
                    self.csv2pd_s = pd.read_csv(dbFile, engine='python', decimal=',', sep=';',encoding="utf-8",
                                header=0, skiprows=[1, 2], index_col=0,
                                usecols =['Date','Time','P1','P2','P3'])
                    self.csv2pd_s = self.csv2pd_s.ix[start_s:end_s]

                else:
            
                    self.boxTableLabel_Strom.setText(self.filename)
                    self.boxDiagramListWidget_Strom.clear()
                    self.csv2pd_s = pd.read_csv(dbFile, engine='python', decimal=',', sep=';',encoding="utf-8",
                                header=0, skiprows=[1, 2], index_col=0,
                                usecols =['Date','Time','P1','P2','P3'])

            
                for column in self.csv2pd_s.columns:
                    self.boxDiagramListWidget_Strom.addItem(column)
        
            # Whole Dataset as Model1
                model11 = mainTableModel.mainTableModel(self.csv2pd_s)
                self.Strom_tab2TableView.setModel(model11)            
            # Status bar
                self.mainStatusbar.showMessage("Import\t" + str(dbFile))
                QMessageBox.information(self, __appname__, "Successfully imported\n " + str(self.csv2pd_s.shape) + " table" )

            else:
                self.filename = ""
            
                time_dlg_w = Ui_Dialog_set_time()
                time_dlg_w.exec_()
                start_date_w, end_date_w = time_dlg_w.returndate()
    
                start_w = QDate.toString(start_date_w, 'dd.MM.yyyy')
                end_w = QDate.toString(end_date_w, 'dd.MM.yyyy')
                print(start_w, end_w, time_dlg_w.result())
                
                
                if time_dlg_w.result():
                    self.boxTableLabel_Wetter.setText(self.filename)
                    self.boxDiagramListWidget_Wetter.clear()
                    self.csv2pd_w = pd.read_csv(dbFile, engine='python', decimal=',', sep='\t',encoding="utf-16", 
                                                usecols = range(1,22), header =0)
                # Split datetime to date and time:
                    self.csv2pd_w[''], self.csv2pd_w['d'] = self.csv2pd_w[''].str[12:20],self.csv2pd_w[''].str[1:11]
                    self.csv2pd_w.set_index('d',inplace=True)
                    self.csv2pd_w = self.csv2pd_w.ix[start_w:end_w]

                else:
                    self.boxTableLabel_Wetter.setText(self.filename)
                    self.boxTableListWidget_Wetter.clear()
    
                    self.csv2pd_w = pd.read_csv(dbFile, engine='python', decimal=',', sep='\t' ,encoding="utf-16", 
                                                usecols = range(1,22), header =0)
                    self.csv2pd_w[''], self.csv2pd_w['d'] = self.csv2pd_w[''].str[12:20],self.csv2pd_w[''].str[1:11]
                    self.csv2pd_w.set_index('d',inplace=True)

                for column in self.csv2pd_w.columns:
                    self.boxDiagramListWidget_Wetter.addItem(column)

            # Whole Dataset as Model1
                model111 = mainTableModel.mainTableModel(self.csv2pd_w)
                self.Wetter_tab2TableView.setModel(model111)            
            # Status bar
                self.mainStatusbar.showMessage("Import\t" + str(dbFile))
                QMessageBox.information(self, __appname__, "Successfully imported\n " + str(self.csv2pd_w.shape) + " table" )
#            except Exception as e:
#                    print(e)
#                    QMessageBox.critical(self, __appname__, "Error importing file, error is\r\n" + str(e))
#                    return

    def plotCSVnewWindow(self):
        #nw = embed_in_qt4_navbar.main()
        # instantiate the ApplicationWindow widget
#        t = np.arange(0.0, 3.0, 0.01)
#        s = np.cos(2*np.pi*t)
#        
#        self.fig= Figure()
#        embed_in_qt4_navbar.Qt4MplCanvas(self).axes.plot(t, s)
        embed_in_qt4_navbar.Qt4MplCanvas(self).draw()
        '''
        self.tab2mpl.canvas.ax.clear()
        zeit = self.csv2pd['Zeit']
        x_max = len(zeit)
        x_num =np.arange(x_max)
        self.tab2mpl.canvas.ax.set_xticks(np.arange(x_max))
        self.tab2mpl.canvas.ax.set_xticklabels(zeit, rotation=45)
        
        y = self.csv2pd['108 <TOF_au?en_Ost_rot> (C)']

        #self.tab2mpl.canvas.ax.locator_params(nbins=10, axis='x')

        self.tab2mpl.canvas.ax.plot(x_num, y)
        
        self.tab2mpl.canvas.draw()
        
        '''
        self.nw = embed_in_qt4_navbar.ApplicationWindow()
        self.nw.show()

#    def DplotCSV_s(self):

    def plotCSV_s(self):
        # Plot in Diagram and print summary the plotted Data
        #settime = timeset.Ui_Dialog_set_time(self)
        #settime.exec_() 
        #execute the dialog
        try:
            self.Strom_tab2mpl.canvas.ax.clear()
            self.Strom_tab2mpl.canvas.ax.get_yaxis().grid(True)
            self.Strom_tab2mpl.canvas.ax.get_xaxis().grid(True)
    # Use Zeit as X-axis:
            self.zeit = self.csv2pd_s['d'].astype(str) + '\t'+ self.csv2pd_s['Zeit'].astype(str)
            x_max = len(self.zeit)
            self.x_num =np.arange(x_max)
    # Multiple select of rows
            self.boxDiagramListWidget_Strom.setSelectionMode(QAbstractItemView.MultiSelection)
            selItems = self.boxDiagramListWidget_Strom.selectedItems()
        # empty datafram
            df_sum = pd.DataFrame().fillna(0) # with 0s rather than NaNs

            summary = self.csv2pd_s.describe()
        
            all_y =[]
            for i in range(len(selItems)):
                self.y = self.csv2pd_s[str(selItems[i].text())].astype(float)
                all_y.append(self.y)
    # Summary of the Data as Model2
                df_sum[str(selItems[i].text())] = summary[str(selItems[i].text())]

            model22 = mainTableModel.mainTableModel(df_sum)
            self.Strom_tab2SummaryTab.setModel(model22)
    # Set time labels to x-axis 
            self.Strom_tab2mpl.canvas.ax.set_xticks(self.x_num)
            self.Strom_tab2mpl.canvas.ax.set_xticklabels(self.zeit, rotation=45)
            self.Strom_tab2mpl.canvas.ax.locator_params(nbins=10, axis='x')
    # Plot and draw in canvas
            for self.y in all_y:
                self.Strom_tab2mpl.canvas.ax.plot(self.x_num, self.y)
            #self.tab2mpl.canvas.ax.plot(x_num, y, 'g',label=self.csv2pd_s.columns[selItem])
            self.Strom_tab2mpl.canvas.ax.legend(loc =0)
            self.Strom_tab2mpl.canvas.draw()
    # Status Bar
            if len(selItems)>1:
                self.mainStatusbar.showMessage("plot multiple diagrams from Stromzähler file")
            else:
                selItem = self.boxDiagramListWidget_Strom.currentRow()
                self.mainStatusbar.showMessage("plot diagram for\t"+ "<"+self.csv2pd_s.columns[selItem]+">")
        except Exception as e : 
            print('Invaild input:', e)
            print('please try again')         

    def plotCSV_w(self):
        # Plot in Diagram and print summary the plotted Data    
        self.Wetter_tab2mpl.canvas.ax.clear()
        self.Wetter_tab2mpl.canvas.ax.get_yaxis().grid(True)
        self.Wetter_tab2mpl.canvas.ax.get_xaxis().grid(True)
    # Use Zeit as X-axis:
        self.zeit = self.csv2pd_w.index + '\t'+ self.csv2pd_w['Zeit'].astype(str)    
        # print(type(self.zeit))

        x_max = len(self.zeit)
        self.x_num =np.arange(x_max)
    # Multiple select of rows
        self.boxDiagramListWidget_Wetter.setSelectionMode(QAbstractItemView.MultiSelection)
        selItems = self.boxDiagramListWidget_Wetter.selectedItems()
        # empty datafram
        df_sum = pd.DataFrame().fillna(0) # with 0s rather than NaNs
        summary = self.csv2pd_w.describe()
        
        all_y =[]
        for i in range(len(selItems)):
            self.y = self.csv2pd_w[str(selItems[i].text())].astype(float)
            all_y.append(self.y)
    # Summary of the Data as Model222
            df_sum[str(selItems[i].text())] = summary[str(selItems[i].text())]
            
        model222 = mainTableModel.mainTableModel(df_sum)
        self.AG_tab2SummaryTab.setModel(model222)
    # Set time labels to x-axis 
        self.Wetter_tab2mpl.canvas.ax.set_xticks(self.x_num)
        self.Wetter_tab2mpl.canvas.ax.set_xticklabels(self.zeit, rotation=45)
        self.Wetter_tab2mpl.canvas.ax.locator_params(nbins=10, axis='x')
    # Plot and draw in canvas
        for self.y in all_y:
            self.Wetter_tab2mpl.canvas.ax.plot(self.x_num, self.y)
        #self.tab2mpl.canvas.ax.plot(x_num, y, 'g',label=self.csv2pd_w.columns[selItem])
        self.Wetter_tab2mpl.canvas.ax.legend(loc =0)
        self.Wetter_tab2mpl.canvas.draw()
    # Status Bar
        if len(selItems)>1:
            self.mainStatusbar.showMessage("plot multiple diagrams from Wetterstation file")
        else:
            selItem = self.boxDiagramListWidget_Wetter.currentRow()
            self.mainStatusbar.showMessage("plot diagram for\t"+ "<"+self.csv2pd_w.columns[selItem]+">")
    
    def plotCSV(self):
        try:
        # Plot in Diagram and print summary the plotted Data    
            self.AG_tab2mpl.canvas.ax.clear()
            self.AG_tab2mpl.canvas.ax.get_yaxis().grid(True)
            self.AG_tab2mpl.canvas.ax.get_xaxis().grid(True)
        
        # Use Zeit as X-axis:
            self.zeit  = self.csv2pd.index + '\t'+ self.csv2pd['Zeit'].astype(str)
            
            x_max = len(self.zeit)
            self.x_num =np.arange(x_max)
            
        # Multiple select of rows
            
            self.boxDiagramListWidget_AG.setSelectionMode(QAbstractItemView.MultiSelection)
            selItems = self.boxDiagramListWidget_AG.selectedItems()
            # empty datafram
            df_sum = pd.DataFrame().fillna(0) # with 0s rather than NaNs
            
            summary = self.csv2pd.describe()
            
            all_y =[]
            for i in range(len(selItems)):
                self.y = self.csv2pd[str(selItems[i].text())].astype(float)
                all_y.append(self.y)

        # Summary of the Data as Model2
                df_sum[str(selItems[i].text())] = summary[str(selItems[i].text())]
                
            model2 = mainTableModel.mainTableModel(df_sum)
            self.AG_tab2SummaryTab.setModel(model2)
            
            '''
            y = self.csv2pd[str(self.csv2pd.columns[selItem])].astype(float)
            '''
            #self.tab2mpl.canvas.ax.xaxis.get_major_locator().set_params(nbins=10)
            #self.tab2mpl.canvas.ax.xaxis.set_major_locator(mticker.MaxNLocator(nbins=10))

        # Set time labels to x-axis 
            self.AG_tab2mpl.canvas.ax.set_xticks(self.x_num)
            self.AG_tab2mpl.canvas.ax.set_xticklabels(self.zeit, rotation=45)
            self.AG_tab2mpl.canvas.ax.locator_params(nbins=10, axis='x')
#            self.AG_tab2mpl.canvas.ax.legend(loc='best')
#            self.AG_tab2mpl.canvas.ax.set_autoscale_on(True)
        # Plot and draw in canvas
            for self.y in all_y:
                self.AG_tab2mpl.canvas.ax.plot(self.x_num, self.y)
        
            #self.tab2mpl.canvas.ax.plot(x_num, y, 'g',label=self.csv2pd.columns[selItem])
            self.AG_tab2mpl.canvas.ax.legend(loc =0)
            
            self.AG_tab2mpl.canvas.draw()
            
        # Status Bar
            if len(selItems)>1:
                self.mainStatusbar.showMessage("plot multiple diagrams from Agilent file")
            else:
                selItem = self.boxDiagramListWidget_AG.currentRow()
                self.mainStatusbar.showMessage("plot diagram for\t"+ "<"+self.csv2pd.columns[selItem]+">")
        except Exception as e : 
            print('Invaild input:', e)
            print('please try again') 

    def tab1Med_apply(self):
        
        #if self.tab1Med_combo_HCir.te
        text = self.tab1Med_combo_HCir.currentText()
        self.tab1Med_label.setText(text)
        #print(self.tab1Med_combo_HCir.currentIndex())
        n=0
        incomp= str('INCOMP::GKN-')
        temp =273.15
        #temp = float(self.tab1Med_line_temp.text())
        pressure =101325
        #pressure = float(self.tab1Med_line_P.text())
        while n!=self.tab1Med_combo_HCir.currentIndex():
            n+=1
        else:
            incomp += str(n*5+20)+str('%')
        
        return incomp
        
    def calculateQ(self):

        start = time.time()
        self.csv2pd.reset_index(inplace=True)
        self.df_Q = self.csv2pd[['d','Zeit']]
        
        rows = self.csv2pd.shape[0]
        
        Agil_list = ["Q_BMA_Ost","Q_BMA_S眉d","Q_BMA_West","Q_BMA_Dach","Q_Solekreis","Q_Heizkreis"]
        for i in range(6):
            column=str(Agil_list[i]+'(kW)')
            delta_T = self.csv2pd.iloc[:,i*2+25] - self.csv2pd.iloc[:,i*2+24]
            avg_T = (self.csv2pd.iloc[:,i*2+25] + self.csv2pd.iloc[:,i*2+24])/2 
            v_flow = self.csv2pd.iloc[:,i+2]

            self.df_Q['Temperature difference'+'\n' +'('+ str(Agil_list[i])+')'] = delta_T
            self.df_Q['average Temperature'+'\n' +'('+ str(Agil_list[i])+')'] = avg_T
            self.df_Q[column]=np.nan

        
            for j in range(rows):
                T = self.df_Q['average Temperature'+'\n' +'('+ str(Agil_list[i])+')'][j]+273.15
                self.df_Q[column][j]= self.df_Q['Temperature difference'+'\n' +'('+ str(Agil_list[i])+')'][j] * PropsSI(
                        'D','T',T,'P',101325,self.tab1Med_apply()) * PropsSI('C','T',T,'P',101325, self.tab1Med_apply()) * v_flow[j] /60000000

        self.csv2pd.set_index('d',inplace=True)
        self.df_Q.set_index('d',inplace=True)
        
        self.model3 = mainTableModel.mainTableModel(self.df_Q)
        self.AG_tab2CalcTab.setModel(self.model3)
        end = time.time()
        tooktime=int(end-start)
        
        for column in self.df_Q.columns:
            self.AG_tab2CalcTab.addItem(column)

    # Status bar
        QMessageBox.information(self, __appname__, "Successfully calculated heat flow rate" + "\n" + "Calculation took" + ": " + str(tooktime) + "seconds")
        self.mainStatusbar.showMessage("Successfully calculated heat flow rate")

        
#    def update_graph(self):
#        try :
#            self.mpl.canvas.axes.clear()
#            self.mpl.canvas.axes.grid(True) 
#            a= [a for a in np.arange(self.num1, self.num2+self.num3, self.num3)]
#            if self.radioButton_5.isChecked():
#                
#                self.mpl.canvas.axes.plot(a, self.Hblist)
#            elif self.radioButton_6.isChecked():
#                    self.mpl.canvas.axes.plot(a, self.Vplist)
#            self.mpl.canvas.draw()
            
        
#        except Exception as e :
#            print('Invaild input: ', e)
#            print('please try again')    
        
#    def calculateQ(self):
#
#        start = time.time()
##        try:
#        self.csv2pd.reset_index(inplace=True)
#    
#        #df_Q = pd.DataFrame(np.random.randint(low=1, high=10, size=(5, 5)), columns=['a','d','c','s','f'],index=['A','B','C','D','E'])
#        df_Q = self.csv2pd[['d','Zeit']]
#        #df_Q.reset_index(inplace=True)
#        #df_Q = pd.DataFrame()
#    
#        rows = self.csv2pd.shape[0]
#    
#        #print(df_Q['Zeit'][2])
#    
#        Agil_list = ["Q_BMA_Ost","Q_BMA_Süd","Q_BMA_West","Q_BMA_Dach","Q_Solekreis","Q_Heizkreis"]
#        for i in range(6):
#
#            column=str(Agil_list[i]+'(kW)')
#            delta_T = self.csv2pd.iloc[:,i*2+25] - self.csv2pd.iloc[:,i*2+24]
#            avg_T = (self.csv2pd.iloc[:,i*2+25] + self.csv2pd.iloc[:,i*2+24])/2 
#            v_flow = self.csv2pd.iloc[:,i+2]
#            
#        
##            df_Q['Temperature difference'+'\n' +'('+ str(Agil_list[i])+')'] = delta_T
#            df_Q.loc['Temperature difference'+'\n' +'('+ str(Agil_list[i])+')'] = delta_T
##            df_Q['average Temperature'+'\n' +'('+ str(Agil_list[i])+')'] = avg_T
#            df_Q.loc['average Temperature'+'\n' +'('+ str(Agil_list[i])+')'] = avg_T
##            df_Q[column]=np.nan
#            df_Q.loc[column]=str(np.nan)
##            np.nan=df_Q.loc[column]
#
#    
#            for j in range(rows):
##                T = df_Q['average Temperature'+'\n' +'('+ str(Agil_list[i])+')'][j]+273.15
#                T = df_Q.loc['average Temperature'+'\n' +'('+ str(Agil_list[i])+')', str(j)]+273.15
#
##                df_Q[column][j]= df_Q['Temperature difference'+'\n' +'('+ str(Agil_list[i])+')'][j] * PropsSI(
##                        'D','T',T,'P',101325,self.tab1Med_apply()) * PropsSI('C','T',T,'P',101325, self.tab1Med_apply()) * v_flow[j] /60000000
#                df_Q.loc[column, j]= df_Q.loc['Temperature difference'+'\n' +'('+ str(Agil_list[i])+')', str(j)] * PropsSI(
#                        'D','T',T,'P',101325,self.tab1Med_apply()) * PropsSI('C','T',T,'P',101325, self.tab1Med_apply()) * v_flow[j] /60000000
#            #df_Q[column][j]= df_Q[column][j] / 60000 * v_flow[j] / 1000
#    
#            
#        #df_Q.join(series_Q.to_frame())
#    #df_Q.set_index('d',inplace=True)
#    
#        model3 = mainTableModel.mainTableModel(df_Q)
#        self.AG_tab2CalcTab.setModel(model3)
#        end = time.time()
#
#    #print(self.tab1Med_apply())
#
#
## Status bar
#        self.mainStatusbar.showMessage("Successfully calculated heat flow rate ----- Calculation took" + "\s" + 
#                                    int(end - start) + "seconds")
                                        

    def plot1(self):
#        self.wow=self.boxTableLabel_AG.text()
#        print(self.wow)
#        if self.wow[0] == 'b':
#            
#            if self.filename[0]=='A':
                
                self.stackedWidget.setCurrentIndex(0)
                self.tabWidget_Agilent.setCurrentIndex(2)
    def plot2(self):
            self.stackedWidget.setCurrentIndex(1)
            self.tabWidget_Strom.setCurrentIndex(2)
    def plot3(self):
        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget_Strom.setCurrentIndex(2)

        
class embedqt4(Main):
    def __init__(self, parent=None):
        super().__init__(self)
        csvpd = self.csv2pd
        # print(len(csvpd['Zeit']))


def main():
    app = QApplication(sys.argv)
    app.setStyle("plastique")
    form = Main()
    form.show()

    app.exec_()
    
if __name__ == "__main__":
    main()






