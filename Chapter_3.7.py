# 3.7 QProgressBar

# setValue() 메서드로 진행 표시줄의 진행 상태를 특정 값으로 설정할 수 있음
# reset() 메서드는 초기 상태로 되돌림

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        # 진행표시줄을 활성화하기 위해 타이머 객체를 사용
        self.timer = QBasicTimer()
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    # 각각의 QObject와 그 자손들은 timerEvent() 이벤트 핸들러를 갖음
    # 이벤트에 반응하기 위해 이벤트 핸들러를 재구성
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step+1
        self.pbar.setValue(self.step)

    # 타이머를 시작하고 멈추도록
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            # 타이머 이벤트를 실행하기 위해, start() 메서드를 호출
            # 첫번째는 종료시간 두 번째는 이벤트가 수행될 객체
            self.timer.start(100, self)
            self.btn.setText('Stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())