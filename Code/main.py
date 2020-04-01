import MegaforceAVR as Megaforce
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

class MainWindow(QMainWindow):
    global projectConfigLocation
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
        self.logs = QPlainTextEdit(self.frame3)

        self.logs.resize(self.frame3.frameGeometry().width() + 50, self.frame3.frameGeometry().height()/2)
        self.frame3.resize(50, 25)

        self.frame3.setStyleSheet("background-color: rgb(40, 40, 40)")

        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font.setPointSize(12)
        self.logs.setFont(font)
        self.logs.setReadOnly(True)
        self.logs.setStyleSheet(
        """QPlainTextEdit {background-color: #333;
                           color: #00FF00;
                           font-family: Courier;}""")

        self.frame5 = QFrame()
        self.frame5.resize(50, 25)
        self.Save = QPushButton('Save', self.frame5)
        self.Save.clicked.connect(self.saveFile)
        self.Load = QPushButton('Load', self.frame5)
        self.Load.clicked.connect(self.openFile)
        self.Setup = QPushButton('Setup', self.frame5)
        self.Upload = QPushButton('Upload',self.frame5)
        self.Upload.clicked.connect(self.UploadToBoard)
        self.Compile = QPushButton('Compile', self.frame5)
        self.Compile.clicked.connect(self.CompileProject)

        self.Save.move(0, 0)
        self.Load.move(0, 30)
        self.Setup.move(0, 60)
        self.Upload.move (0, 90)
        self.Compile.move(0,120)
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

    @pyqtSlot()
    def saveFile(self):
        self.logs.insertPlainText("saving\n")
        text = self.getText()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.logs.insertPlainText("Save to: " )
        file = open(fileName, 'w')
        self.logs.insertPlainText(file.name + "\n")
        file.write(text)
        file.close()
        self.logs.insertPlainText("Saved successfully! \n")

    @pyqtSlot()
    def openFile(self):
        self.editor.clear()
        self.editor.insertPlainText("")
        self.logs.insertPlainText("Opening \n")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        self.logs.insertPlainText("Opening file:")
        if fileName:
            self.logs.insertPlainText(fileName + "\n")

        file = open (fileName, 'r')
        self.editor.insertPlainText(file.read())
        file.close()
        self.logs.insertPlainText("File read successfully \n")

    @pyqtSlot()
    def CompileProject(self):
        self.logs.insertPlainText("Compiling started :")
        if (Megaforce.Compile("atmega328","")) == 0:
            self.logs.insertPlainText("\n ERROR COMPILING - NO file detected\n")
        else:
            self.logs.insertPlainText("\nCompile succesfull\n")


    @pyqtSlot()
    def UploadToBoard(self):
        self.logs.insertPlainText("Uploading started :")
        if (Megaforce.Upload("atmega328", "","","","")) == 123:
            self.logs.insertPlainText("\n ERROR Uploading - NO config file detected\n")
        else:
            self.logs.insertPlainText("\nUpload succesfull\n")
def tmp():
    FILELOCATIONS = ['/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/main.c']#,
                     #'/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/MMINIT.c',
                    # '/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/systime.c']
    CPU = "atmega328pb"
    Megaforce.Compile(CPU,FILELOCATIONS)

    CPUTYPE = "m328pb"
    PROGTYPE = "arduino"
    PROGLOCATION = "/dev/ttyUSB0"
    BAUD = "115200"
    PROJECTLOCATION = "/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/project.hex"



if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = MainWindow()

    sys.exit(app.exec_())