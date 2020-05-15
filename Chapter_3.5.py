# 3.5 QComboBox

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)

        # QComboBox 위젯 생성, addItem() 메서드를 이용해서 선택 가능한 4개의 옵션들을 추가가
        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50,50)

        # 옵션을 선택하면 onActivated() 메서드 호출
        cb.activated[str].connect(self.onActivated)

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()


    def onActivated(self, text):
        # 선택한 항목의 텍스트가 라벨에 나타나도록 하고, adjustSize() 메서드를 이용해서 라벨의 크기를 자동으로 조절하도록 함함
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())