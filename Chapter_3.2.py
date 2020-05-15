# 3.2 QLabel
# 텍스트 또는 이미지 라벨을 만들 때 사용
# 사용자와 어떤 상호작용을 제공하지는 않음

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QLabel 위젯 작성 생성자에 라벨 텍스트, 부모 위젯을 입력
        label1 = QLabel('First Label', self)
        # setAlignment() 메서드로 라벨의 배치를 설정
        # Qt.AlignCenter로 설정하면 수평 수직 방향 모두 가운데 위치
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignVCenter)

        # 라벨에 사용될 폰트를 하나 생성
        font1 = label1.font()
        font1.setPointSize(20)

        font2 = label2.font()
        # 폰트 종류 선택
        font2.setFamily('Times New Roman')
        # 폰트 진하게 설정
        font2.setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())