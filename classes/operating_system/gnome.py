import uuid
from classes.operating_system.shortcut import Shortcut
from classes.operating_system.terminal import Terminal
from models.detailed_delays import DetailedDelays

class Gnome:
    global_running_stack: list[str] = []

    def __init__(self, launch_command:str):
        self.global_id:str = str(uuid.uuid4())
        self.launch_command:str = launch_command

    def _launch(self, global_id):

        if self._is_running_global(global_id):
            self._active_global()
        else:
            Terminal.quick_launch(
                self.launch_command,
                detailed_delays=DetailedDelays(delay_terminal=1, delay_typing=1, delay_confirm=0))
            self.global_running_stack.insert(0, global_id)

    def _active_global(self):
        if not self._is_active_window_global():
            self.__relocate_to_active_global()


    def _is_active_window_global(self) -> bool:
        return self.global_id in self.global_running_stack and self.global_running_stack[0] == self.global_id

    def _is_running_global(self, global_id:str) -> bool:
        return global_id in self.global_running_stack

    def __relocate_to_active_global(self) -> None:
        current_index = self.global_running_stack.index(self.global_id)
        Shortcut.lx_cycle_windows(current_index, 2)
        self.global_running_stack.insert(0, self.global_running_stack.pop(current_index))