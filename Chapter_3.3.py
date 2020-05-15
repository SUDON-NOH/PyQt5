# 3.3 QCheckBox

# QCheckBox 위젯은 on(체크됨)/off(체크안됨)의 두 상태를 갖는 버튼을 제공
# 체크 박스가 선택되거나 해제될 때, stateChanged() 시그널을 발생
# 체크 박스의 선택 여부를 확인하기 위해서 isChecked() 메서드를 사용, 선택 여부에 따라 boolean 값을 반환

# setTristate() 메서드를 사용하면 '변경 없음(no change)' 상태를 가질 수 있음
# 체크 박스의 상태를 얻기 위해서는 checkState() 메서드를 사용
# 선택/변경 없음/해제 여부에 다라서 2/1/0 값을 반환

# QButtonGroup 클래스를 사용하면 여러 개의 버튼을 묶어서 exclusive/non-exclusive 버튼 그룹을 만들 수 있음
# exclusive 버튼 그룹은 여러 개 중 하나의 버튼만 선택할 수 있음

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Show Title 이라는 텍스트 라벨을 갖는 체크박스를 만듦
        cb = QCheckBox('Show Title', self)
        cb.move(20, 20)
        # 체크박스는 디폴트로 체크가 되어있지 않은 off 상태로 나타나기 때문에 on 상태로 바꾸기 위해 toggle() 메서드를 사용
        cb.toggle()
        # 체크박스의 상태가 바뀔 때 발생하는 시그널을 우리가 정의한 changeTitle() 메서드에 연결
        cb.stateChanged.connect(self.changeTitle)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())