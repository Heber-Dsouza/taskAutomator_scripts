import pyautogui as mouse_click

def print_position():
    mouse_click.sleep(3)
    print(mouse_click.position())


if __name__ == '__main__':
    print_position()