# 1.3 창닫기버튼
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Push 버튼 생성
        # 첫번째 파라미터에는 버튼이 표시될 텍스트를 입력, 두번째 파라미터에는 버튼이 위치할 부모 위젯을 입력
        btn = QPushButton('Quit', self)
        btn.move(1230,750)
        btn.resize(btn.sizeHint())
        # 버튼을 클릭하면 'clicked' 시그널이 만들어짐
        # 'clicked' 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결됨
        # 발신자와 수신자 두 객체 간에 커뮤니케이션이 이루어짐
        btn.clicked.connect(QCoreApplication.instance().quit)

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


