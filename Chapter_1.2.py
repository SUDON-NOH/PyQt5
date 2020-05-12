# 1.2 아이콘 넣기
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ybio')
        self.setWindowIcon(QIcon('ybio.png'))
        # 순서대로 창의 위치: x, y 창의 너비와 높이: x, y
        # 창 띄우기에서 move()와 resize() 메서드를 합쳐놓은 것과 같음.
        self.setGeometry(300, 100, 1360, 800)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())