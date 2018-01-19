import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(seft):
        super().__init__()
        
        seft.initUI()
        
    def initUI(seft):
        
        seft.setGeometry(300,300,300,220)
        seft.setWindowTitle('Icon')
        seft.setWindowIcon(QIcon('opengraph-icon-200x200.png'))
        
        seft.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())