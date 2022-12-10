from controller import *
from PyQt5 import *

def main():
    app = QApplication([])
    ui = Controller()
    ui.show()
    app.exec_()
    

if __name__ == "__main__":
    main()