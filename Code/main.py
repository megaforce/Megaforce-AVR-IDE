import MegaforceAVR as Megaforce
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
import ConfigHandler as handler

class Setup(QMainWindow):
    def __init__(self, parent=None):
        super(Setup, self).__init__(parent)
        self.setWindowTitle("Megaforce Setup Wizard")
        self.left = 50
        self.top = 50
        self.width = 670
        self.height = 300
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet("background-color: rgb(55, 55, 55)")
        self.form_widget = SetupLayout(self)
        self.setCentralWidget(self.form_widget)

class SetupLayout(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        layout = QGridLayout()
        self.left = QFrame(self)
        self.left.setStyleSheet("background-color: rgb(90, 90, 90)")
        self.rightBottom = QFrame(self)
        self.rightBottom.setStyleSheet("background-color: rgb(90, 90, 90)")
        self.rightTop = QFrame(self)
        self.rightTop.setStyleSheet("background-color: rgb(90, 90, 90)")
        self.filesInProject = QPlainTextEdit(self.rightTop)
        self.filesInProject.resize(self.rightTop.frameGeometry().width() + 90, self.rightTop.frameGeometry().height() + 110)
        layout.addWidget(self.left,0,0, 2, 5)
        layout.addWidget(self.rightTop, 0, 5, 1, 2)
        layout.addWidget(self.rightBottom,1,5,1,2)


        self.Confirm = QPushButton('Confirm',self.rightBottom)
        self.Confirm.clicked.connect(self.ConfirmConfig)
        self.Clear = QPushButton('Clear', self.rightBottom)
        self.Clear.move(0,40)

        self.form = QFormLayout(self.left)

        self.CPU = QLineEdit()
        self.CPUTYPE = QLineEdit()
        self.PROGTYPE = QLineEdit()
        self.PROGLOCATION = QLineEdit()
        self.BAUD = QComboBox()


        baudrates = [
            self.tr('9600'),
            self.tr('115200')
        ]
        self.BAUD.addItems(baudrates)

        self.form.addRow(QLabel('Long CPU name'), self.CPU)
        self.form.addRow(QLabel('Short CPU name'), self.CPUTYPE)

        self.form.addRow(QLabel('Programtor'), self.PROGTYPE)
        self.form.addRow(QLabel('Com port'), self.PROGLOCATION)
        self.form.addRow(QLabel('BAUD'),self.BAUD)

        self.AddFile = QPushButton()
        self.AddFile.setObjectName("Search")
        self.AddFile.setText("Search")
        self.AddFile.clicked.connect(self.addFileIntoProject)
        self.form.addRow(QLabel('ADD FILE'), self.AddFile)
        self.setLayout(layout)

        self.show()

    @pyqtSlot()
    def addFileIntoProject(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)

        file = str(fileName)
        self.filesInProject.insertPlainText("#" +file +" ?\n")
    @pyqtSlot()
    def ConfirmConfig(self):
        string =""
        config = self.filesInProject.toPlainText()
        for j in range (config.find("#")+1,config.find("?")-1):
                string += config[j]
        f = open("programFile.txt", "w")
        string = string.replace(os.path.basename(string),'CONFIG.txt')
        f.write(string)
        f.close()
        string = string.replace(os.path.basename(string), 'project.hex')
        f = open(string,"w")
        f.close()
        f = open(string,"w")
        tmp =   """CPU =#ENDCPU
FILELOCATIONS =#ENDFILELOCATIONS
CPUTYPE =#ENDCPUTYPE
PROGTYPE =#ENDPROGTYPE
PROGLOCATION =#ENDPROGLOCATION
BAUD =#ENDBAUD
PROJECTLOCATION =#ENDPROJECTLOCATION"""
        f.write(tmp)
        f.close()
        handler.BuildConfigFile(self.CPU.text(),self.filesInProject.toPlainText(),self.CPUTYPE.text(),self.PROGTYPE.text(),self.PROGLOCATION.text(),self.BAUD.currentText())

    @pyqtSlot()
    def ClearConfig(self):
        self.filesInProject.clear()
        self.PROGLOCATION = self.PROGTYPE = self.CPUTYPE =  self.CPU = ""

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(250, 250, 1000, 1000)
        self.setWindowTitle("Megaforce AVR IDE")
        self.setStyleSheet("background-color: rgb(90, 90 , 90)")
        self.form_widget = Ui(self)
        self.setCentralWidget(self.form_widget)

        mainMenu = self.menuBar()
        mainMenu.setStyleSheet("background-color: rgb(55, 55, 55)")
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

    def fileOpen(self):
        print()
    def fileSave(self):
        print()
    def __Compile(self):
        print()
    def __Upload(self):
        print()

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
        self.frame.setStyleSheet("background-color: rgb(90, 90, 90)")

        self.frame2 = QFrame()
        self.frame2.resize(50, 50)
        self.frame2.setStyleSheet("background-color: rgb(90, 90, 90)")

        self.frame4 = QFrame()
        self.frame4.resize(50, 25)
        self.frame4.setStyleSheet("background-color: rgb(90, 90, 90)")

        self.treeview = QTreeView(self.frame4)
        self.listview = QListView(self.frame2)
        path = QDir.rootPath()
        print("\n"+path)
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

        self.logs.resize(self.frame3.frameGeometry().width() + 60, self.frame3.frameGeometry().height()/2 + 20)
        self.frame3.resize(50, 25)

        self.frame3.setStyleSheet("background-color: rgb(90, 90, 90)")

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
        self.New = QPushButton('New file', self.frame5)
        self.Save = QPushButton('Save', self.frame5)
        self.Save.clicked.connect(self.saveFile)
        self.Load = QPushButton('Load', self.frame5)
        self.Load.clicked.connect(self.openFile)
        self.Setup = QPushButton('Setup', self.frame5)
        self.Setup.clicked.connect(self.SetupProject)
        self.Upload = QPushButton('Upload',self.frame5)
        self.Upload.clicked.connect(self.UploadToBoard)
        self.Compile = QPushButton('Compile', self.frame5)
        self.Compile.clicked.connect(self.CompileProject)

        self.New.move(0,0)
        self.Save.move(0, 30)
        self.Load.move(0, 60)
        self.Setup.move(0, 90)
        self.Upload.move (0, 120)
        self.Compile.move(0,150)
        self.frame5.setStyleSheet("background-color: rgb(90, 90, 90)")

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
        print(fileName)
        fileName = os.path.dirname(os.path.abspath(fileName))
        print(fileName)
        self.listview.setRootIndex(self.fileModel.setRootPath(fileName))


        tmp = 0
        for i in range (0,len(fileName)):
            tmp += 1
            if(fileName[len(fileName) - 1 - i] == "/"):
                tmp -= 1
                fileName = fileName[:-tmp]
                break
        print(fileName)
        self.treeview.setRootIndex(self.dirModel.index(fileName))



    @pyqtSlot()
    def CompileProject(self):
        file = open("programFile.txt", 'r')
        f = file.read()
        self.logs.insertPlainText("Compiling started :")
        if (Megaforce.Compile(f)) == 123:
            self.logs.insertPlainText("\n ERROR COMPILING - Empty config file detected\n")
        else:
            self.logs.insertPlainText("\nCompile succesfull\n")


    @pyqtSlot()
    def UploadToBoard(self):
        file = open("programFile.txt", 'r')
        f = file.read()
        self.logs.insertPlainText("Uploading started :")
        if (Megaforce.Upload(f)) == 123:
            self.logs.insertPlainText("\n ERROR Uploading - Empty config file detected\n")
        else:
            self.logs.insertPlainText("\nUpload succesfull\n")

    @pyqtSlot()
    def SetupProject(self):
        file = open("programFile.txt", 'r')
        f = file.read()
        file.close()
        self.logs.insertPlainText("Setup wizard started\n")
        dialog = Setup(self)
        dialog.show()

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
    f = open("programFile.txt", "w")
    f.close()
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = MainWindow()
    sys.exit(app.exec_())
