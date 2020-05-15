# 3.1 QPushButton

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 푸시 버튼 생성, 첫 파라미터는 버튼에 나타날 텍스트, 두 번째 파라미터는 버튼이 속할 부모 클래스를 지정
        # '&' 이게 들어가면 그 뒤에 글자가 단축키가 되어 Alt+b 가 단축키가 됨
        btn1 = QPushButton('&Button1', self)
        # setCheckable() 을 True로 설정하면 선택되거나 선택되지 않은 상태를 유지
        btn1.setCheckable(True)
        # toggle() 메서드를 호출하면 버튼의 상태가 변함, 따라서 이 버튼은 프로그램이 시작될 때 선택되어 있음
        btn1.toggle()

        # setText() 메서드로 텍스트 지정 가능
        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        # setEnabled() 를 False로 설정하면 버튼은 사용할 수 없게 됨
        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


