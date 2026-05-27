from classes.core.keyboard import Keyboard
from classes.operating_system.shortcut import Shortcut
from models.detailed_delays import DetailedDelays

class Terminal:
    @staticmethod
    def quick_launch(
            launch_command:str,
            delay:float|int|None=None,
            detailed_delays:DetailedDelays|None=None
    )->bool:

        try:
            Shortcut.lx_terminal(getattr(detailed_delays, "delay_terminal", delay or 0))
            Keyboard.type(launch_command, getattr(detailed_delays, "delay_typing", delay or 0))
            Keyboard.confirm(getattr(detailed_delays, "delay_confirm", delay or 0))
            return True
        except Exception as error:
            print(error)
            return False
