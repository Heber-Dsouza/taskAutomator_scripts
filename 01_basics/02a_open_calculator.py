from classes.mouse import Mouse
from classes.keyboard import Keyboard

def init():
    Mouse.left_click(2395, 1052)
    Keyboard.type("calculator", 1)
    Keyboard.confirm()

if __name__ == '__main__':
    init()