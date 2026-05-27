import pyautogui as keyboard

class Keyboard:

    KEYS = {k: k for k in keyboard.KEYBOARD_KEYS}

    @staticmethod
    def type(text: str, delay:float|int = 0):
        """Write a text

        Args:
          text (str): the text you want to type
          delay (float | int, optional): Time to wait before writing the text. Defaults to 0.
        Returns:
          None
        """
        keyboard.sleep(delay)
        keyboard.typewrite(text)

    @staticmethod
    def confirm(delay:float|int=0):
        """Press enter to confirm

        Args:
          delay (float | int, optional): Time to wait before press enter. Defaults to 0.
        Returns:
          None
        """
        keyboard.sleep(delay)
        keyboard.press(Keyboard.KEYS['enter'], 1)