import time
from enum import Enum
from classes.core.keyboard import Keyboard
from classes.operating_system.shortcut import Shortcut
from models.IN.detailed_delays import DetailedDelays

class LaunchOperationTypes(Enum):
    NORMAL = "NORMAL"
    BACKGROUND = "BACKGROUND"
    NOHUP = "NOHUP"
    DISOWN = "DISOWN"

class Terminal:
    @staticmethod
    def __handle_exec_format(launch_command:str, operation_type:LaunchOperationTypes, instant_exit:bool=True)->str:
        result = ""
        match operation_type:
            case operation_type.BACKGROUND:
                result += f"{launch_command} &{" exit" if instant_exit else ""}"
            case operation_type.NOHUP:
                result += f"nohup {launch_command} &{" exit" if instant_exit else ""}"
            case operation_type.DISOWN:
                result += f"{launch_command} & disown{" & exit" if instant_exit else ""}"
            case _:
                result = launch_command
        return result



    @staticmethod
    def quick_launch(
            launch_command:str,
            delay:float|int|None=None,
            detailed_delays:DetailedDelays|None=None
    )->bool:

        try:
            Shortcut.lx_terminal(getattr(detailed_delays, "delay_terminal", delay or 0))
            Keyboard.type(Terminal.__handle_exec_format(
                launch_command,
                LaunchOperationTypes.NOHUP
            ), getattr(detailed_delays, "delay_typing", delay or 0))
            Keyboard.confirm(getattr(detailed_delays, "delay_confirm", delay or 0))

            # This delay is important to allow the application
            # to open before another routine retrieves the active window ID.
            time.sleep(getattr(detailed_delays, "post_wait_delay", delay or 0))
            return True
        except Exception as error:
            print(error)
            return False
