import uuid
from classes.operating_system.application import Application
from classes.core.keyboard import Keyboard

class Calculator(Application):
    def __init__(self):
        super().__init__("nohup gnome-calculator & exit")

    def sum(self, x:int, y:int):
        if not self.is_active_window():
            self.run()
        Keyboard.type(f"{x}+{y}", 2)
        Keyboard.confirm()
