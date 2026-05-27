from classes.operating_system.application import Application
from classes.core.keyboard import Keyboard

class Writer(Application):
    def __init__(self):
        super().__init__("lowriter")

    def type_text(self, x:int, y:int):
        self.open()
        Keyboard.type("Hello World!", 1)
