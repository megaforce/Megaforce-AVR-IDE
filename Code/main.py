import MegaforceAVR as Megaforce
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(250, 250, 800, 700)
        self.setWindowTitle("Megaforce AVR IDE")

        self.form_widget = Ui(self)
        self.setCentralWidget(self.form_widget)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Aplication')
        Tools = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)

        issuesButton = QAction(QIcon('exit24.png'), 'Report an error', self)
        aboutButton = QAction(QIcon('exit24.png'), 'About', self)

        compileButton =  QAction(QIcon('exit24.png'), 'Compile', self)
        compileButton.setShortcut('F7')
        compileButton.setStatusTip('Compiles the project')

        uploadButton = QAction(QIcon('exit24.png'), 'Upload', self)
        uploadButton.setShortcut('F8')
        uploadButton.setStatusTip('Uploads the project')

        setupButton = QAction(QIcon('exit24.png'), 'Setup', self)
        setupButton.setShortcut('F6')
        setupButton.setStatusTip('Sets up the project')

        saveButton = QAction(QIcon('exit24.png'), 'Save', self)
        saveButton.setShortcut('Ctrl+S')
        saveButton.setStatusTip('Save current progress')

        loadButton = QAction(QIcon('exit24.png'), 'Load', self)

        helpMenu.addAction(aboutButton)
        helpMenu.addAction(issuesButton)
        fileMenu.addAction(loadButton)
        fileMenu.addAction(saveButton)
        fileMenu.addAction(exitButton)
        Tools.addAction(setupButton)
        Tools.addAction(compileButton)
        Tools.addAction(uploadButton)

        self.show()
    def __save(self):
        print("Saving")
    def __load(self):
        print("Loading")
    def __Compile(self):
        Megaforce.Comile("Test","test")
    def __Upload(self):
        Megaforce.Upload('test',"test","test","test","m")

class Ui(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setGeometry(300,300,1280,800)

        self.frame = QFrame()
        self.frame.resize(10,10)
        self.frame.setStyleSheet("background-color: rgb(200, 255, 255)")

        self.frame2 = QFrame()
        self.frame2.resize(50, 50)
        self.frame2.setStyleSheet("background-color: rgb(0, 255, 255)")

        self.frame3 = QFrame()
        self.frame3.resize(50, 50)
        self.frame3.setStyleSheet("background-color: rgb(0, 0, 255)")

        self.frame4 = QFrame()
        self.frame4.resize(50, 50)
        self.frame4.setStyleSheet("background-color: rgb(50, 255, 255)")

        layout=QGridLayout()
        layout.addWidget(self.frame,0,0)
        layout.addWidget(self.frame2,0, 1, 1, 3)
        layout.addWidget(self.frame3 ,1, 0, 1, 0)
        layout.addWidget(self.frame4,1, 2, 1, 3)

        self.setLayout(layout)

def tmp():
    FILELOCATIONS = ['/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/main.c',
                     '/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/MMINIT.c',
                     '/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/systime.c']
    CPU = "atmega328pb"

    CPUTYPE = "m328pb"
    PROGTYPE = "arduino"
    PROGLOCATION = "/dev/ttyUSB0"
    BAUD = "115200"
    PROJECTLOCATION = "/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/project.hex"

    Megaforce.TestBoard(CPUTYPE, PROGTYPE, PROGLOCATION, BAUD)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = MainWindow()

    sys.exit(app.exec_())