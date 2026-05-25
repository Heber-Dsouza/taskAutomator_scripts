import pyautogui as kboard
from classes.keyboard import Keyboard

class Shortcut:
    @staticmethod
    def lx_show_apps(delay: float|int = 0):
        """Open 'Show Application' linux modal

        Args:
          delay (float | int, optional): Time to wait before performing the shortcut. Defaults to 0.
        Returns:
          None
        """
        kboard.sleep(delay)
        kboard.shortcut(Keyboard.KEYS['win'], Keyboard.KEYS['a'])

    @staticmethod
    def lx_terminal(delay: float | int = 0):
        """Open 'Show Application' linux modal

        Args:
          delay (float | int, optional): Time to wait before performing the shortcut. Defaults to 0.
        Returns:
          None
        """
        kboard.sleep(delay)
        kboard.shortcut(Keyboard.KEYS['win'], Keyboard.KEYS['t'])