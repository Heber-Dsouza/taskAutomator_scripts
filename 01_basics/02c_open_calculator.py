from classes.keyboard import Keyboard
from classes.shortcut import Shortcut

def init():
    Shortcut.lx_terminal(1)
    Keyboard.type("gnome-calculator", 1)
    Keyboard.confirm()

if __name__ == '__main__':
    init()