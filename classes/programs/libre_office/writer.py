import uuid

from classes.operating_system.application import Application
from classes.core.keyboard import Keyboard

class Writer(Application):
    global_id:str = str(uuid.uuid4())
    running_stack:list[str] = []

    def __init__(self):
        super().__init__("lowriter", self.global_id, self.running_stack)

    def type_text(self, x:int, y:int):
        self.open()
        Keyboard.type("Hello World!", 1)
