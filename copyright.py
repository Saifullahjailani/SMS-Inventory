import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QTextEdit

# License text (replace this with the MIT license text if you have it)
license_text = """
<b>MIT License</b><br><br>

Copyright (c) [year] [author]<br><br>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:<br><br>

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.<br><br>

<b>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</b>
"""


class LicenseDialog(QDialog):
    def __init__(self):
        super().__init__(flags=Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        self.setWindowTitle("MIT Open Source License Viewer")
        layout = QVBoxLayout(self)

        text_edit = QTextEdit(self)
        text_edit.setReadOnly(True)
        text_edit.setHtml(license_text)

        layout.addWidget(text_edit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = LicenseDialog()
    dialog.exec_()
    sys.exit(app.exec_())
