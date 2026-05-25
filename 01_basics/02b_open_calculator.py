from classes.keyboard import Keyboard
from classes.shortcut import Shortcut

def init():
    Shortcut.lx_show_apps(1)
    Keyboard.type("calculator", 1)
    Keyboard.confirm()

if __name__ == '__main__':
    init()