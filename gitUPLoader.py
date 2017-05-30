#! /usr/bin/env python
#__author__= 'Hussam Ashraf'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import subprocess
import os
import sys

class git(QWidget):

    def __init__(self):
        super(git, self).__init__()

        QApplication.setStyle(QStyleFactory.create('palstique'))
        self.setWindowTitle('GitLoader')
        self.setStyleSheet(

"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}"

)
        self.setMinimumWidth(500)
        self.setMaximumWidth(500)
        self.setMinimumHeight(600)
        self.setMaximumHeight(600)


        self.body()

    def body(self):

    ### labels section

        self.folderDir = QLabel('Folder Path', self)
        self.folderDir.setGeometry(10, 25 , 100, 20)


        self.remote = QLabel('Git Remote', self)
        self.remote.setGeometry(10, 75 , 100, 20)


        self.e_mail = QLabel('E-Mail', self)
        self.e_mail.setGeometry(10, 175 , 100, 20)

        self.usrNme = QLabel('User Name', self)
        self.usrNme.setGeometry(10, 125 , 100, 20)


        self.passwd = QLabel('Password', self)
        self.passwd.setGeometry(10, 225 , 100, 20)





    ### texts section

        self.folderDirT = QLineEdit(self)
        self.folderDirT.setGeometry(80, 20, 400, 30)
        self.folderDirT.setPlaceholderText('Enter your project directory')

        self.remoteT = QLineEdit(self)
        self.remoteT.setGeometry(80, 70, 400, 30)
        self.remoteT.setPlaceholderText('The git remote... command from your github account')

        self.usrNmeT = QLineEdit(self)
        self.usrNmeT.setGeometry(80, 120, 400, 30)


        self.e_mailT = QLineEdit(self)
        self.e_mailT.setGeometry(80, 170, 400, 30)




        self.passwdT = QLineEdit(self)
        self.passwdT.setGeometry(80, 220, 400, 30)
        self.passwdT.setEchoMode(QLineEdit.Password)





######################################
    #buttons section
        pushBtn = QPushButton('Push To GITHUB', self)
        pushBtn.setGeometry(55, 330, 120, 30)
        pushBtn.clicked.connect(self.push)

        pushBtn.setCursor(QCursor(Qt.PointingHandCursor))

        extBtn = QPushButton('Exit the program', self)
        extBtn.setGeometry(330, 330, 120, 30)
        extBtn.clicked.connect(self.closeApp)
        extBtn.setCursor(QCursor(Qt.PointingHandCursor))

        stsBtn = QPushButton('Status', self)
        stsBtn.setGeometry(110, 280, 120, 30)
        stsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        stsBtn.clicked.connect(self.gitStatus)

        addBtn = QPushButton('Add Files', self)
        addBtn.setGeometry(270, 280, 120, 30)
        addBtn.setCursor(QCursor(Qt.PointingHandCursor))
        addBtn.clicked.connect(self.addToRepo)


    #### result
        self.textShow = QTextEdit(self)
        self.textShow.setGeometry(10, 400, 480, 200)
        self.textShow.setStyleSheet('QWidget {font-size:15px;}')
        self.textShow.setReadOnly(True)



###############################
## Created Methodes
    @pyqtSlot()
    def closeApp(self):
        msgbox = QMessageBox.question(self, 'Exiting!!!', 'Are you sure?!!', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

        if msgbox == QMessageBox.Yes:
            self.close()
        else:
            pass


    def gitStatus(self):

        try:
            os.chdir(self.folderDirT.text())
            if '.git' not in os.listdir() :

                subprocess.check_output('git init', shell=True)
                subprocess.check_output('git config --global user.email %s' %self.e_mailT.text())
                subprocess.check_output('git config --global user.name %s' %self.usrNmeT.text())


            status = str(subprocess.check_output('git status', shell=True))
            status = status.replace('\\n', ' ')
            status = status.replace('\\t', ' ')

            self.textShow.setText(status[2:-1])
        except:
                self.err = error()
                self.err.show()


    def addToRepo(self):
        try:
            subprocess.check_output('git add *')
            subprocess.check_output('git commit -m "commit"')
        except:
            self.addErr = addError()
            self.addErr.show()


    def push(self):


        try:
            try:

                try:
                    subprocess.check_output('%s' %self.remoteT.text())

                    remoteTxt = self.remoteT.text()

                    subprocess.check_output('git push https://{}:{}@{}' .format(self.usrNmeT.text(), self.passwdT.text(), remoteTxt[remoteTxt.find('//')+2 :]), shell=True)

                    self.textShow.setText('Pushed To {}'.format(remoteTxt[remoteTxt.find('h'):]))

                except :

                    try:
                        subprocess.check_output('%s' %self.remoteT.text())
                    except:
                        pass
                    finally:
                        subprocess.check_output('git push -u origin master')
                        self.textShow.setText('Pushed To {}'.format(remoteTxt[remoteTxt.find('h'):]))
            except:
                self.textShow.setText('Everything is up to date')


        except:
            self.err = error()
            self.err.show()

######################################################
### Errors classes

class error(QWidget): # if error happened
    def __init__(self):
        super (error, self).__init__()
        self.setWindowFlags(Qt.Popup)
        self.setStyleSheet('QWidget {background-color:gray; color:white; font-size:15px; font-weight:bold; font-family:MV Boli}')
        self.resize(400, 50)

        errLbl = QLabel(self)
        errLbl.setText('Something went wrong !!!\nPlease check your information and try again.')
        errLbl.move(20, 5)

class addError(QWidget):# if the user didn't intialize git first
        def __init__(self):
            super (addError, self).__init__()
            self.setWindowFlags(Qt.Popup)
            self.setStyleSheet('QWidget {background-color:gray; color:white; font-size:15px; font-weight:bold; font-family:MV Boli}')
            self.resize(400, 50)

            errLbl = QLabel(self)
            errLbl.setText('Please Click Status button first.')
            errLbl.move(60, 10)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = git()
    window.show()
    sys.exit(app.exec_())
