import pyautogui as mouse

class Mouse:
    @staticmethod
    def print_position(delay:float|int=3):
        mouse.sleep(delay)
        print(mouse.position())

    @staticmethod
    def left_click(x:int, y:int, delay:float|int=0, number_clicks:int=1, interval:int=0):
        """
        Performs a left click.

        Args:
            x (int): X position value.
            y (int): Y position value.
            delay (int, optional): Time to wait before performing the click. Defaults to 0.
            number_clicks (int, optional): Number of clicks to perform. Defaults to 1.
            interval (int, optional): Time interval between clicks if ``number_clicks`` is greater than 1. Defaults to 0.

        Returns:
            None
        """
        mouse.sleep(delay)
        mouse.click(x, y, number_clicks, interval)