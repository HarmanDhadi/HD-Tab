import gemini
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea
)

from PyQt6.QtCore import Qt


class ChatWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jarvis")
        self.resize(700, 550)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.setWindowOpacity(0.95)


        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)


        # Chat area
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.scroll.setStyleSheet("""
            QScrollArea {
                border:none;
                background:transparent;
            }
        """)


        self.chat_widget = QWidget()

        self.chat_layout = QVBoxLayout()
        self.chat_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.chat_widget.setLayout(self.chat_layout)

        self.scroll.setWidget(self.chat_widget)



        # Input area
        bottom_layout = QHBoxLayout()


        self.input_box = QLineEdit()

        self.input_box.setPlaceholderText(
            "Ask me anything..."
        )


        self.input_box.setStyleSheet("""
            QLineEdit {
                background:rgba(60,60,60,200);
                color:white;
                border-radius:18px;
                padding:12px;
                font-size:16px;
            }
        """)



        self.send_button = QPushButton("➜")

        self.send_button.setFixedSize(55,45)


        self.send_button.setStyleSheet("""
            QPushButton {
                background:#4f8cff;
                color:white;
                border-radius:18px;
                font-size:20px;
            }
        """)


        bottom_layout.addWidget(self.input_box)
        bottom_layout.addWidget(self.send_button)


        main_layout.addWidget(self.scroll)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)



        self.send_button.clicked.connect(self.send_message)
        self.input_box.returnPressed.connect(self.send_message)



    def add_message(self, text, sender):

        bubble = QLabel(text)

        bubble.setWordWrap(True)
        bubble.setMaximumWidth(450)


        bubble.setStyleSheet("""
            QLabel {
                background:#555555;
                color:white;
                border-radius:15px;
                padding:10px;
                font-size:16px;
            }
        """)


        row = QHBoxLayout()


        if sender == "user":

            row.addStretch()
            row.addWidget(bubble)

        else:

            row.addWidget(bubble)
            row.addStretch()


        self.chat_layout.addLayout(row)


        QApplication.processEvents()

        self.scroll.verticalScrollBar().setValue(
            self.scroll.verticalScrollBar().maximum()
        )


        return bubble



    def send_message(self):

        text = self.input_box.text().strip()


        if text == "":
            return


        # Show user message
        self.add_message(
            "You: " + text,
            "user"
        )


        self.input_box.clear()


        # Temporary loading message
        thinking = self.add_message(
            "Jarvis: Thinking...",
            "ai"
        )


        QApplication.processEvents()


        try:

            # Ask Gemini
            answer = gemini.ask_gemini(text)


            # Replace thinking text
            thinking.setText(
                "Jarvis: " + answer
            )


        except Exception as e:

            thinking.setText(
                "Jarvis error:\n" + str(e)
            )
def voice_message(self, text, sender):

    self.add_message(
        text,
        sender
    )


if __name__ == "__main__":



    app = QApplication(sys.argv)

    window = ChatWindow()
    window.show()

    sys.exit(app.exec())