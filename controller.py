
from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Controller, self).__init__()
        self.setupUi(self)
        self.rock_button.clicked.connect(lambda: self.display_image("rock.jpg"))
        self.paper_button.clicked.connect(lambda: self.display_image("paper.jpg"))
        self.scissors_button.clicked.connect(lambda: self.display_image("scissors.jpg"))
        self.lizard_button.clicked.connect(lambda: self.display_image("lizard.jpg"))
        self.spock_button.clicked.connect(lambda: self.display_image("spock.jpg"))
        
   
    def display_image(self, image: str):
        '''
        This function displays an image either left or right, depending on which button is checked
        :param image: This is the image file path that will be displayed
        '''
        if self.radio_button1.isChecked():
            self.p1_image.setPixmap(QtGui.QPixmap(image))
        else:
            self.p2_image.setPixmap(QtGui.QPixmap(image))
        