import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QScrollArea, QLabel, QSizePolicy, QFrame, QGraphicsDropShadowEffect
from PyQt5.QtGui import QFont, QPalette, QBrush, QImage, QIcon, QColor
from PyQt5.QtCore import Qt

class ChatWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("المستخدم")
        self.resize(800, 600)
        self.setWindowIcon(QIcon("C:/Users/A/OneDrive/Bureau/robot/hssm.jpg"))
        self.background_image = QImage("C:/Users/A/OneDrive/Bureau/robot/html.jpg")
        self.scaled_image = self.background_image.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(self.scaled_image))
        self.setPalette(palette)

        self.chat_scroll = QScrollArea()
        self.chat_scroll.setWidgetResizable(True)
        self.chat_content = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_content)
        self.chat_layout.addStretch(1)
        self.chat_scroll.setWidget(self.chat_content)

        self.user_input = QTextEdit()
        self.send_button = QPushButton("Send")

        self.chat_scroll.setStyleSheet("background: transparent; border: none;")
        self.chat_content.setStyleSheet("background: transparent;")
        
        self.user_input.setStyleSheet("""
            padding: 8px;
            border: 2px solid #007CFF;
            border-radius: 20px;
            margin: 10px;
            background-color: rgba(255, 255, 255, 0.9);
            color: #333;
            font-family: Arial, sans-serif;
            font-size: 14px;
        """)

        self.user_input.setFixedHeight(60)

        self.send_button.setStyleSheet("""
            padding: 10px 20px;
            background-color: #007CFF;
            color: #ffffff;
            border: 2px solid #4CAF50;
            border-radius: 25px;
            cursor: pointer;
            font-family: Arial, sans-serif;
            font-size: 14px;
        """)
        self.send_button.setFixedHeight(50)

        self.chat_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.user_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.send_button.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.chat_scroll)
        
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.user_input)
        input_layout.addWidget(self.send_button)
        input_layout.setContentsMargins(10, 10, 10, 10)

        main_layout.addLayout(input_layout)
        self.setLayout(main_layout)
        self.user_input.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_widget = ChatWidget()
    chat_widget.show()
    sys.exit(app.exec_())
