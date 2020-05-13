# 1.9 시간 형식
# 날짜 표시하기
from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()
print(now.toString())

now = QDate.currentDate()
print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('yyyy-MM-dd'))
print(now.toString(Qt.ISODate))
# 2020-05-12

print(now.toString(Qt.DefaultLocaleLongDate))

# 시간 표시하기
from PyQt5.QtCore import QTime, Qt

time = QTime.currentTime()
print(time.toString())
print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString('hh.mm.ss.zzz'))
print(time.toString(Qt.DefaultLocaleLongDate))
print(time.toString(Qt.DefaultLocaleShortDate))

# 날짜 + 시간

from PyQt5.QtCore import QDateTime, Qt

datetime = QDateTime.currentDateTime()
print(datetime.toString())

datetime = QDateTime.currentDateTime()
print(datetime.toString('d.m.yy hh:mm:ss'))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print(datetime.toString(Qt.DefaultLocaleShortDate))

# 상태표시줄에 날짜 표시하기

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDateTime, Qt

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleShortDate))

        self.setWindowTitle('Ybio')
        self.setGeometry(300, 300, 400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

