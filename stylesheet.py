TABLE_STYLE = "QTableWidget::item {\n" \
              + "    background-color: #f0f0f0; /* Set the default background color for table items */\n" \
              + "}\n" \
              + "\n" \
              + "QTableWidget::item:nth-child(even) {\n" \
              + "    background-color: #ffffff; /* Set the background color for even rows */\n" \
              + "}\n" \
              + "\n" \
              + "QTableWidget::item:hover {\n" \
              + "    background-color: #c0c0c0; /* Set the background color for hovered items */\n" \
              + "}"

TEXT_BOX_STYLE = "QLineEdit {\n" \
                 + "    background-color: #ffffff; /* Set the background color */\n" \
                 + "    border: 2px solid #555555; /* Set the border style */\n" \
                 + "    border-radius: 5px; /* Set the border radius */\n" \
                 + "    padding: 5px; /* Set the padding */\n" \
                 + "    color: #000000; /* Set the text color */\n" \
                 + "    font-size: 12px; /* Set the font size */\n" \
                 + "}"
BUTTON_STYLE = "QPushButton {\n" \
               + "    background-color: #4d4d4d;\n" \
               + "    color: #ffffff;\n" \
               + "    padding: 8px 16px;\n" \
               + "    border-radius: 20px;\n" \
               + "}\n" \
               + "\n" \
               + "QPushButton:hover {\n" \
               + "    background-color: #595959;\n" \
               + "}\n" \
               + "\n" \
               + "QPushButton:pressed {\n" \
               + "    background-color: #3d3d3d;\n" \
               + "}"

# Apply style sheet to the combo box
COMBOX_BOX_STYLE = """
    QComboBox {
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 5px;
        border-radius: 5px;
        font-size: 14px;
        color: #333333;
    }
    
"""


def get_opacity(opacity):
    return "QPushButton {\n" \
        + f"    background-color: rgba(77, 77, 77, {opacity});\n" \
        + "    color: #ffffff;\n" \
        + "    padding: 8px 16px;\n" \
        + "    border-radius: 20px;\n" \
        + "}\n" \
        + "\n" \
        + "QPushButton:hover {\n" \
        + "    background-color: #595959;\n" \
        + "}\n" \
        + "\n" \
        + "QPushButton:pressed {\n" \
        + "    background-color: #3d3d3d;\n" \
        + "}"
