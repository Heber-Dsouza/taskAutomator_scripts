from classes.keyboard import Keyboard
from classes.shortcut import Shortcut
import uuid

class Calculator:

    running_stack: list[str] = []

    def __init__(self):
        self.id = str(uuid.uuid4())

    def run(self):
        Shortcut.lx_terminal(1)
        if self.is_running and not self.is_active_window():
            self.__relocate_to_active()
        else:
            Keyboard.type("nohup gnome-calculator & exit", 1)
            self.running_stack.insert(0, self.id)

    def sum(self, x:int, y:int):
        if not self.is_running:
            self.run()
        Keyboard.type(f"{x}+{y}", 2)
        Keyboard.confirm()

    def is_active_window(self) -> bool:
        return self.running_stack[0] == self.id

    def is_running(self) -> bool:
        return self.id in self.running_stack

    def __relocate_to_active(self) -> None:
        self.running_stack.insert(0, self.running_stack.pop(self.running_stack.index(self.id)))
