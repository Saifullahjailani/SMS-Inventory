import sys
import logic.config as config
import config_ui
import logic.db
import customerGui
import homeWindowGui
import productsWindowGui
from PyQt5 import QtWidgets
import logic.config as conf


#
class Data:
    def __init__(self, app):
        self.app = app
        self._db = None
        self._receipts_path = None
        self.homeWindow = homeWindowGui.HomeWindow(self)
        self.customerWindow = customerGui.CustomerWindow(self)
        self.productsWindow = productsWindowGui.ProductsWindow(self)
        self.window = QtWidgets.QMainWindow()

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, val):
        self._db = val

    @property
    def receipts_path(self):
        return self._receipts_path

    @receipts_path.setter
    def receipts_path(self,value):
        self._receipts_path = value

    def draw(self, ui):
        ui.setupUi(self.window)
        self.window.show()

    def exit(self):
        sys.exit(self.app.exec_())

def show_config():
    dialog: QtWidgets.QDialog = config_ui.Dialog()
    dialog.show()
    dialog.exec_()
    return conf.read()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    config = conf.read()
    while config is None:
        config = show_config()
    data = Data(app)
    data.db = logic.db.DB(config.db_name, config.db_user, config.db_password, config.db_host, config.db_port)
    if not data.db.connect():
        config = show_config()
        data.db = logic.db.DB(config.db_name, config.db_user, config.db_password, config.db_host, config.db_port)
    data.db.disconnect()
    data.receipts_path = config.receipts_dir
    try:
        data.draw(data.homeWindow)
    except:
        data.db.disconnect()
    finally:
        data.exit()
