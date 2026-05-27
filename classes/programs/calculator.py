from classes.operating_system.application import Application
from classes.core.keyboard import Keyboard

class Calculator(Application):
    def __init__(self):
        super().__init__("gnome-calculator")

    def sum(self, x:int, y:int):
        self.open()
        Keyboard.type(f"{x}+{y}", 2)
        Keyboard.confirm()
