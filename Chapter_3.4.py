# 3.4 QRadioButton
# 사용자가 선택할 수 있는 버튼을 만들 때 사용

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QRadioButton을 만듦 라벨에 들어갈 텍스트와 부모 위젯을 입력
        rbtn1 = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        # 프로그램이 실행될 때 버튼이 선택되어 표시
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

