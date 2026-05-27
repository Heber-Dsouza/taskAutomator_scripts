import uuid

from classes.operating_system.application import Application
from classes.core.keyboard import Keyboard

class Calculator(Application):
    global_id = str(uuid.uuid4())
    running_stack:list[str] = []

    def __init__(self):
        super().__init__("gnome-calculator", self.global_id, self.running_stack)

    def sum(self, x:int, y:int):
        self.open()
        Keyboard.type(f"{x}+{y}", 2)
        Keyboard.confirm()
