#!/usr/bin/env python

# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui
#from MA_main import *
# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

# import the NavigationToolbar Qt4Agg widget
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib as mpl
# Matplotlib Figure object
from matplotlib.figure import Figure
import plot1
import matplotlib.image as mpimg
#import MA_UII
#import MA_main 

class MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self):
        # setup Matplotlib Figure and Axis
        self.fig = plt.figure()
        
        self.ax = self.fig.add_subplot(111)
#        self.fig.tight_layout()
        self.fig.set_tight_layout(True)
        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # we define the widget as expandable
        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)

    def mouseDoubleClickEvent(self,event): 
        self.save1()
    def save1(self):
        
#        self.Strom_tab2mpl.canvas.save('aaa.png')
#        a = plot.MplCanvas
        plot1.MplCanvas(self).draw()
        self.show_window = plot1.ApplicationWindow()
        self.show_window.show()
       
#        self.canvas.show()
#        self.fig.save('lena_new_sz.png')
#        self.sender.plotWindow()
#        print(self.sender)
#        self.nw1 = plot1.ApplicationWindow()
#        self.nw1.canvas.draw()
#        plt.savefig("examples.jpg")  

#        if sender  == 
#        plt.show()

#        plot1.Qt4MplCanvas(self).draw()
        print('mouse double clicked')
        # set the layout to the vertical box

class MplWidget(QtGui.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent = None):
        # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
        
        mpl.rcParams['xtick.direction'] = 'in' 
        mpl.rcParams['ytick.direction'] = 'in' 
        # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas()
#        mpl.rc('xtick', labelsize=7)
        # create a vertical box layout
        self.vbl = QtGui.QVBoxLayout()
        # add mpl widget to the vertical box
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        
        
class ApplicationWindow(QtGui.QMainWindow):
    """Example main window"""
    def __init__(self):
        # initialization of Qt MainWindow widget
        QtGui.QMainWindow.__init__(self)
        # set window title
        self.setWindowTitle("Matplotlib Figure")

        # instantiate a widget, it will be the main one
        self.main_widget1 = QtGui.QWidget(self)

        # create a vertical box layout widget
        vbll = QtGui.QVBoxLayout(self.main_widget1)
        # instantiate our Matplotlib canvas widget
        qmc1 = Qt4MplCanvas(self.main_widget1)
        # instantiate the navigation toolbar
        ntb1 = NavigationToolbar(qmc1, self.main_widget1)
        # pack these widget into the vertical box
        vbll.addWidget(qmc1)
        vbll.addWidget(ntb1)

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
    MA_main.save(x,y)
    app = QApplication(sys.argv)
    app.setStyle("plastique")
#    form = Main()
#    form.show()
    app.exec_()

        
