import pyautogui as mouse
from typing import Final
from classes.core.sound import Sound, LaunchOperationTypes
from models.IN.beep_setting import BeepSetting
from classes.utils.numeric_match import NumericMatch

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

    @staticmethod
    def move_to_position(x:int|None, y:int|None, delay:float|int=0, duration:float|int=0.0):
        """
        Performs a left click.

        Args:
            x (int, optional): X position value. Defaults to None.
            y (int, optional): Y position value. Defaults to None.
            delay (int, optional): Time to wait before performing the click. Defaults to 0.
            duration (float, int, optional): The amount of time it takes to move the mouse to xy coordinates.
                If 0, then the mouse cursor is moved instantaneously. 0.0 by default.
        Returns:
            None
        """
        mouse.sleep(delay)
        mouse.moveTo(x, y, duration)

    @staticmethod
    def get_position(wait_time:float|int, play_sound:bool=False, beep_settings:BeepSetting|None=None) -> mouse.Point:
        """
        Performs a left click.

        Args:
            wait_time (float | int): Time to wait before getting the current cursor position.
            play_sound (bool, optional): Whether to play a sound before capturing the cursor position.
                Defaults to False.
            beep_settings (BeepSetting, optional): customize beep frequency and quantity. Defaults to None.

        Returns:
            None
        """

        if not play_sound:
            mouse.sleep(wait_time)
            position = mouse.position()
            print(position)
            return position

        default_beep_quantity:Final = 3
        default_beep_frequency:Final = 0.3
        default_max_beep_quantity:Final = 5
        default_min_frequency:Final = 0.1
        default_max_frequency:Final = 1.0

        quantity: int = (
            beep_settings.quantity % default_max_beep_quantity
            if (
                    beep_settings
                    and beep_settings.quantity
            )
            else default_beep_quantity
        )
        frequency: float | int = (
            NumericMatch.is_in_range(
                default_min_frequency,
                default_max_frequency,
                beep_settings.frequency
            ) or default_max_frequency
            if beep_settings and beep_settings.frequency
            else default_beep_frequency
        )

        preparation_time = wait_time * frequency
        wait_time -= preparation_time
        preparation_time /= float(quantity)

        mouse.sleep(wait_time)

        for i in range(quantity):
            Sound.play_alert()
            mouse.sleep(preparation_time)

        position = mouse.position()
        print(position)
        Sound.play_alert(LaunchOperationTypes.SUCCESS)


        return position