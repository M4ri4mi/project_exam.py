from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout

class Calculator(QDialog):  # Inherit from QDialog instead of QWidget
    def __init__(self, parent=None):  
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(300, 400)  # Set fixed size

        self.expression_line = QLineEdit()
        self.expression_line.setReadOnly(True)

        self.buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '←', '+'],
            ['=', 'C']
        ]

        self.create_layout()

    def create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.expression_line)

        for row in self.buttons:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(lambda _, text=button_text: self.on_button_click(text))
                row_layout.addWidget(button)
            layout.addLayout(row_layout)

        self.setLayout(layout)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.expression_line.text())
                self.expression_line.setText(str(result))
            except Exception as e:
                self.expression_line.setText("Error")
        elif text == 'C':
            self.expression_line.clear()
        elif text == '←':
            current_text = self.expression_line.text()
            self.expression_line.setText(current_text[:-1])
        else:
            self.expression_line.setText(self.expression_line.text() + text)
