from classes.keyboard import Keyboard
from classes.shortcut import Shortcut

class Calculator:
    is_running: bool = False

    def run(self):
        Shortcut.lx_terminal(1)
        if self.is_running:
            pass # goto calculator
        else:
            Keyboard.type("nohup gnome-calculator & exit", 1)
            self.is_running = True
            Keyboard.confirm()

    def sum(self, x:int, y:int):
        if not self.is_running:
            self.run()
        Keyboard.type(f"{x}+{y}", 2)
        Keyboard.confirm()