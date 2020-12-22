import sys # to launch application
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyBx4_TYfj5L9xxg2Cjfo03f8mYu3ejvYgg",
    'authDomain': "pyqtauth.firebaseapp.com",
    'databaseURL': "https://pyqtauth-default-rtdb.firebaseio.com/",
    'projectId': "pyqtauth",
    'storageBucket': "pyqtauth.appspot.com",
    'messagingSenderId': "801352196245",
    'appId': "1:801352196245:web:ef8dc458f8fd6f1de3fb9c",
    'measurementId': "G-WNHG5LW6Q9"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi(r"C:\Users\sonik\Documents\QT Apps\Login forms\login.ui", self)
        # by loading the ui, the objects of that ui are now objects of this class, hence self.loginButton
        self.loginButton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createAcc.clicked.connect(self.gotoCreate)
        self.loginButton.clicked.connect(self.loginfunction)
        self.err_invalidemail.setVisible(False)
        self.login_success.setVisible(False)
    
    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        try:
            auth.sign_in_with_email_and_password(email,password)
            self.login_success.setVisible(True)
        except:
            self.err_invalidemail.setVisible(True)
    
    def gotoCreate(self):           # to open the createacc page when clicked on create account button
        createacc = CreateAccount()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1) # to move forward in the stack and navigate to another page

class CreateAccount(QDialog):
    def __init__(self):
        super(CreateAccount, self).__init__()
        loadUi(r"C:\Users\sonik\Documents\QT Apps\Login forms\createacc.ui", self)
        self.signupButton.clicked.connect(self.createAccFunc)        
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)        
        self.err_invalidemail.setVisible(False)
        self.err_nomatchpasswords.setVisible(False)
        self.backto_loginButton.clicked.connect(self.gotoLogin)
    
    def createAccFunc(self):
        email = self.email.text()
        if self.password.text() == self.confirmpassword.text():
            password = self.password.text()
            try:
                auth.create_user_with_email_and_password(email,password)
                # now we should again go back to login page after creating an account
                login = Login()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex()+1)
            except:
                self.err_invalidemail.setVisible(True)
        else:
            self.err_nomatchpasswords.setVisible(True)
            
    def gotoLogin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


# to launch application
app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()         # when we have ultiple pages to navigate, this keeps them in stack
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()