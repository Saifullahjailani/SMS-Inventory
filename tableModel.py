from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data, headers, parent=None):
        super().__init__(parent)
        self._data = data
        self._headers = headers

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        if role == Qt.DisplayRole:
            return str(self._data[row][col])

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._headers[section])
            elif orientation == Qt.Vertical:
                return str(section + 1)

        return None

    def add_row(self, row_data):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._data.append(row_data)
        self.endInsertRows()

    def is_empty(self):
        return len(self._data) == 0

    def get_item(self, index):
        r = index.row()
        return self._data[r]

    def clear(self):
        self._data = []
        self.layoutChanged.emit()

    def change_data(self, data):
        self._data = data
        self.layoutChanged.emit()

    def re_draw(self):
        self.layoutChanged.emit()

    def delete(self, id):
        ids = [x[0] for x in self._data]
        index = ids.index(id)
        self.pop(index)

    def pop(self,idx):
        self.beginRemoveRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._data.pop(idx)
        self.endRemoveRows()
        self.layoutChanged.emit()

    def find(self, id):
        ids = [x[0] for x in self._data]
        if id in ids:
            return ids.index(id)
        return -1
    def sum_col(self, col):
        def sum_():
            total = 0
            for row in self._data:
                total += row[col]
            return round(total,2)

        return sum_

    def set(self, row, index):
        self._data[index] = row
        self.layoutChanged.emit()

    def get_index(self, id):
        ids = [x[0] for x in self._data]
        return ids.index(id)