#!/usr/bin/env python
# NEW WINDOW!!!!!
# for command-line arguments
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui

# Numpy functions for image creation
import numpy as np
import matplotlib.pyplot as plt
# Matplotlib Figure object
from matplotlib.figure import Figure
# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
# import the NavigationToolbar Qt4Agg widget
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import MA_main


class Qt4MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self, parent):

        #MA_main.Main.importedCSV(self)
        # plot definition
        self.fig = plt.figure()
        self.axes = self.fig.add_subplot(111)
        
        
        t = np.arange(0.0, 3.0, 0.01)
        s = np.cos(2*np.pi*t)
        zeit=[' ','a','b','c','d','e','f','g']

        self.axes.locator_params(nbins=9, axis='x')
        #self.axes.get_xaxis().set_ticks(range(3))
        #self.axes.xaxis.get_major_locator().set_params(nbins=3)

        
        
        self.axes.set_xticklabels(zeit)
        
        #self.axes.tick_params(labelbottom='off')  
        self.axes.plot(t, s, 'r', label="CPU1")
        self.axes.set_xlabel("Time (min)")
        self.axes.set_ylabel("Celsius")
        self.axes.set_title("CPU/GPU temperature", fontsize=15)
        self.axes.legend(loc =0)
        
       
        
        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # set the parent widget
        self.setParent(parent)

        # we define the widget as expandable
        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)


class ApplicationWindow(QtGui.QMainWindow):
    """Example main window"""
    def __init__(self):
        # initialization of Qt MainWindow widget
        QtGui.QMainWindow.__init__(self)
        # set window title
        self.setWindowTitle("Matplotlib Figure With NavigationToolbar")

        # instantiate a widget, it will be the main one
        self.main_widget = QtGui.QWidget(self)

        # create a vertical box layout widget
        vbl = QtGui.QVBoxLayout(self.main_widget)
        # instantiate our Matplotlib canvas widget
        qmc = Qt4MplCanvas(self.main_widget)
        # instantiate the navigation toolbar
        ntb = NavigationToolbar(qmc, self.main_widget)
        # pack these widget into the vertical box
        vbl.addWidget(qmc)
        vbl.addWidget(ntb)

        # set the focus on the main widget
        self.main_widget.setFocus()
        # set the central widget of MainWindow to main_widget
        self.setCentralWidget(self.main_widget)


def main():
    
# create the GUI application
    App = QtGui.QApplication(sys.argv)
# instantiate the ApplicationWindow widget
    aw = ApplicationWindow()
# show the widget
    aw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
    App.exec_()
    
if __name__ == "__main__":
    main()

    app = QApplication(sys.argv)
    app.setStyle("plastique")
#    form = Main()
#    form.show()
    app.exec_()
    

