# 1.1 창띄우기

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 타이틀바에 나타나는 창의 제목을 설정
        self.setWindowTitle('Ybio')
        # 위젯을 스크린의 x, y 위치로 이동시킨다.
        self.move(300, 100)
        # 위젯의 크기를 너비 x, 높이 y 로 조절
        self.resize(1360, 800)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

