import sys
import logic.config as config
import logic.db
import customerGui
import homeWindowGui
import productsWindowGui
from PyQt5 import QtWidgets


class Data:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.db = logic.db.DB(config.DB_NAME, config.DB_USER, config.DB_PASSWORD, config.DB_HOST, config.DB_PORT)
        self.homeWindow = homeWindowGui.HomeWindow(self)
        self.customerWindow = customerGui.CustomerWindow(self)
        self.productsWindow = productsWindowGui.ProductsWindow(self)
        self.window = QtWidgets.QMainWindow()
        

    def draw(self, ui):
        ui.setupUi(self.window)
        self.window.show()

    def exit(self):
        sys.exit(self.app.exec_())


        


if __name__ == '__main__':
    data = Data()
    data.draw(data.homeWindow)
    data.exit()