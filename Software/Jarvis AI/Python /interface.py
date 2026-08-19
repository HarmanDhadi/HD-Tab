import json
import os
import sys
import math
import chat_window
import jarvis_command

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import (
    QSize,
    Qt,
    QTimer,
    QPropertyAnimation,
    QEasingCurve
)


app = QApplication(sys.argv)


class FloatingButton(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlag(
            Qt.WindowType.FramelessWindowHint
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.resize(260, 260)


        self.button = QPushButton(self)

        self.button.setGeometry(
            30,
            30,
            200,
            200
        )


        self.normal_icon = QSize(200, 200)
        self.hover_icon = QSize(240, 240)


        self.button.setIcon(
            QIcon(
                r"/Users/harmandhadi/PycharmProjects/PythonProject/PythonProject/Tab-Key/assets/FOR PYCHARM.png"
            )
        )


        self.button.setIconSize(
            self.normal_icon
        )


        self.button.setStyleSheet("""
        QPushButton {
            background: transparent;
            border: none;
        }
        """)


        self.icon_animation = QPropertyAnimation(
            self.button,
            b"iconSize"
        )

        self.icon_animation.setDuration(250)

        self.icon_animation.setEasingCurve(
            QEasingCurve.Type.OutBack
        )


        self.button.enterEvent = self.hover_enter
        self.button.leaveEvent = self.hover_leave


        self.chat = None


        self.button.clicked.connect(
            self.toggle_chat
        )


        self.angle = 0
        self.base_y = 0


        self.timer = QTimer()

        self.timer.timeout.connect(
            self.float_animation
        )

        self.timer.start(30)



    def open_chat(self):

        if self.chat is None:

            self.chat = chat_window.ChatWindow()


        if not self.chat.isVisible():

            self.chat.show()


        self.chat.raise_()

        self.chat.activateWindow()



    def toggle_chat(self):

        if self.chat is None:

            self.chat = chat_window.ChatWindow()

            self.chat.show()


        else:

            if self.chat.isVisible():

                self.chat.close()

            else:

                self.chat.show()



    def animate_icon(self, size):

        self.icon_animation.stop()

        self.icon_animation.setStartValue(
            self.button.iconSize()
        )

        self.icon_animation.setEndValue(
            size
        )

        self.icon_animation.start()



    def hover_enter(self, event):

        self.animate_icon(
            self.hover_icon
        )



    def hover_leave(self, event):

        self.animate_icon(
            self.normal_icon
        )



    def float_animation(self):

        self.angle += 0.08

        movement = math.sin(
            self.angle
        ) * 3


        self.move(
            self.x(),
            int(self.base_y + movement)
        )





floating = FloatingButton()



# Check for voice command
signal_timer = QTimer()


def check_jarvis():

    if jarvis_command.check_signal():

        print("Opening chat window")

        floating.open_chat()



signal_timer.timeout.connect(
    check_jarvis
)

signal_timer.start(500)





# Bottom-left placement

screen = app.primaryScreen().availableGeometry()

margin = 25


x = screen.left() + margin

y = screen.bottom() - floating.height() - margin


floating.base_y = y


floating.move(
    x,
    y
)


floating.show()

def check_messages():

    file = "chat_messages.json"

    if os.path.exists(file):

        with open(file,"r") as f:

            data=json.load(f)


        os.remove(file)


        if floating.chat:

            floating.chat.add_message(
                data["text"],
                data["sender"]
            )



message_timer = QTimer()

message_timer.timeout.connect(
    check_messages
)

message_timer.start(300)


sys.exit(app.exec())