import MegaforceAVR as Megaforce
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(250, 250, 1000, 1000)
        self.setWindowTitle("Megaforce AVR IDE")
        self.setStyleSheet("background-color: rgb(200, 255, 255)")
        self.form_widget = Ui(self)
        self.setCentralWidget(self.form_widget)

        mainMenu = self.menuBar()
        mainMenu.setStyleSheet("background-color: rgb(0qpl, 255, 255)")
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
        saveButton.triggered.connect(self.fileSave)

        loadButton = QAction(QIcon('exit24.png'), 'Load', self)
        loadButton.setStatusTip('Loads a new file')
        loadButton.triggered.connect(self.fileOpen)

        helpMenu.addAction(aboutButton)
        helpMenu.addAction(issuesButton)
        fileMenu.addAction(loadButton)
        fileMenu.addAction(saveButton)
        fileMenu.addAction(exitButton)
        Tools.addAction(setupButton)
        Tools.addAction(compileButton)
        Tools.addAction(uploadButton)

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.end()

    def fileOpen(self):
        print()
    def fileSave(self):
        print()
    def __Compile(self):
        Megaforce.Comile("Test","test")
    def __Upload(self):
        Megaforce.Upload('test',"test","test","test","m")

class Ui(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setGeometry(300,300,1280,800)

        self.frame = QFrame()
        layout = QGridLayout()
        self.editor = QPlainTextEdit(self.frame)
        self.editor.resize(self.frame.frameGeometry().width() + 50, self.frame.frameGeometry().height() + 40)

        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font.setPointSize(12)
        self.editor.setFont(font)
        f = open("/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/main.c", "r")
        self.editor.insertPlainText(f.read())
        self.path = None

        self.frame.resize(100,100)
        self.frame.setStyleSheet("background-color: rgb(200, 255, 255)")

        self.frame2 = QFrame()
        self.frame2.resize(50, 50)
        self.frame2.setStyleSheet("background-color: rgb(0, 255, 255)")

        self.frame4 = QFrame()
        self.frame4.resize(50, 25)
        self.frame4.setStyleSheet("background-color: rgb(255, 105, 0)")

        self.treeview = QTreeView(self.frame4)
        self.listview = QListView(self.frame2)
        path = QDir.rootPath()

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot | QDir.Files)

        self.treeview.setModel(self.dirModel)
        self.listview.setModel(self.fileModel)

        self.treeview.setRootIndex(self.dirModel.index(path))
        self.listview.setRootIndex(self.fileModel.index(path))

        self.treeview.clicked.connect(self.on_clicked)

        self.frame3 = QFrame()
        self.frame3.resize(50, 25)
        self.frame3.setStyleSheet("background-color: rgb(255, 0, 0)")

        self.frame5 = QFrame()
        self.frame5.resize(50, 25)
        self.frame5.setStyleSheet("background-color: rgb(0, 155, 0)")

        layout.addWidget(self.frame,0,0, 2, 5)
        layout.addWidget(self.frame2,1,5,1,2)
        layout.addWidget(self.frame3 ,3, 0, 1, 5)
        layout.addWidget(self.frame4,0, 5, 1, 2)
        layout.addWidget(self.frame5, 3, 5, 1, 2)

        self.setLayout(layout)

    def getText(self):
        return(self.editor.toPlainText())

    def on_clicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.listview.setRootIndex(self.fileModel.setRootPath(path))

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