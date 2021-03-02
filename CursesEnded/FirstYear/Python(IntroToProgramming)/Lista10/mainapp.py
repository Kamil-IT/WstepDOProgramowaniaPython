import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Init number buttons
        self.ui.pushButton_1.clicked.connect(lambda: self.add_to_main_field(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.add_to_main_field(2))
        self.ui.pushButton_3.clicked.connect(lambda: self.add_to_main_field(3))
        self.ui.pushButton_4.clicked.connect(lambda: self.add_to_main_field(4))
        self.ui.pushButton_5.clicked.connect(lambda: self.add_to_main_field(5))
        self.ui.pushButton_6.clicked.connect(lambda: self.add_to_main_field(6))
        self.ui.pushButton_7.clicked.connect(lambda: self.add_to_main_field(7))
        self.ui.pushButton_8.clicked.connect(lambda: self.add_to_main_field(8))
        self.ui.pushButton_9.clicked.connect(lambda: self.add_to_main_field(9))

        # Init action signs
        self.ui.pushButton_minus.clicked.connect(lambda: self.add_to_main_field('-'))
        self.ui.pushButton_plus.clicked.connect(lambda: self.add_to_main_field('+'))
        self.ui.pushButton_star.clicked.connect(lambda: self.add_to_main_field('*'))
        self.ui.pushButton_bravely.clicked.connect(lambda: self.add_to_main_field('/'))

        self.ui.pushButton_equal.clicked.connect(lambda: self.add_counted_score())

        self.ui.radioButtonRed.toggled.connect(lambda: self.change_color())
        self.ui.radioButtonBlue.toggled.connect(lambda: self.change_color())
        self.ui.radioButtonBlack.toggled.connect(lambda: self.change_color())

    def add_to_main_field(self, number):
        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + str(number))

    def add_counted_score(self):
        score = eval(self.ui.textEdit.toPlainText())
        self.ui.textEdit.setText(str(score))

    def change_color(self):
        if self.ui.radioButtonRed.isChecked():
            self.ui.textEdit.setStyleSheet("QTextEdit {color:red}")
        elif self.ui.radioButtonBlue.isChecked():
            self.ui.textEdit.setStyleSheet("QTextEdit {color:blue}")
        elif self.ui.radioButtonBlack.isChecked():
            self.ui.textEdit.setStyleSheet("QTextEdit {color:black}")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
