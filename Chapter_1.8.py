# 1.8 창을 화면 가운데로

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(1360, 800)

        # center 메서드를 통해서 창이 화면의 가운데에 위치하게 됨
        self.center()
        self.show()

    def center(self):
        # frameGeometry 메서드를 통해 창의 위치와 크기 정보를 가져옴
        qr = self.frameGeometry()
        # 모니터 화면의 가운데를 파악
        cp = QDesktopWidget().availableGeometry().center()
        # 창의 위치를 화면의 중심의 위치로 이동
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

