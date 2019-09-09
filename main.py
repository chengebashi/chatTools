import main_req
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = main_req.Mylogin()
    win.show()
    sys.exit(app.exec_())