# 3.6 QLineEdit

# 한 줄의 문자열을 입력하고 수정할 수 있도록 하는 위젯
# echoMode() 를 설정함으로써 '쓰기 전용' 영역으로 사용할 수 있음 - 비밀번호와 같은 입력을 받을 때 유용
# setEchoMode() 메서드로 이러한 모드를 설정할 수 있음.
# Normal 모드를 가장 흔하게 사용 ex) setEchoMode(QLineEdit.Normal) or setEchoMode(0)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        qle = QLineEdit(self)
        qle.setEchoMode(QLineEdit.Password) # 비밀번호 설정
        qle.move(60, 100)
        # qle의 텍스트가 바뀌면 onChanged() 메서드를 호출
        qle.textChanged[str].connect(self.onChanged)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

