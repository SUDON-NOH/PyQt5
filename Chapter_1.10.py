# 1.10 스타일 꾸미기

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # QLabel 클래스를 이용해서 세 개의 라벨 위젯 생성
        # 라벨 텍스트는 각 'Red', 'Green', 'Blue'
        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')

        # 글자색 빨간색, 경계선 실선(solid), 경계선 두께 2px, 경계선 색 #FA8072, 경계선 모서리 3px만큼 둥글게 설정
        lbl_red.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius: 3px")
        lbl_green.setStyleSheet("color: green;"
                                "background-color: #7FFFD4")
        lbl_blue.setStyleSheet("color: blue;"
                               "background-color: #87CEFA;"
                               "border-style: dashed;"
                               "border-width: 3px;"
                               "border-color: #1E90FF")
        # 수직 박스 레이아웃(QVBoxLayout() 을 이용해서 세 개의 라벨 위젯을 수직으로 배치
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        self.setWindowTitle('Ybio')
        self.setGeometry(300,300,300,200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())