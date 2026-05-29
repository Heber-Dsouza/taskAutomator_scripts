from classes.operating_system.shortcut import Shortcut
from classes.operating_system.terminal import Terminal
from classes.core.window import Window
from models.IN.detailed_delays import DetailedDelays

class Gnome(Window):
    global_running_stack: list[str] = []

    def __init__(self, launch_command:str):
        super().__init__()
        self.launch_command:str = launch_command

    def _launch(self, global_id, post_wait_delay:float|int=0):

        if self._is_running_global(global_id):
            self._active_global(global_id)
        else:
            Terminal.quick_launch(
                self.launch_command,
                detailed_delays=DetailedDelays(
                    delay_terminal=1,
                    delay_typing=1,
                    delay_confirm=0,
                    post_wait_delay=post_wait_delay
                )
            )
            self.global_running_stack.insert(0, global_id)

    def _active_global(self, global_id:str):
        if not self._is_running_global(global_id):
            self._launch(global_id)
        if not self._is_active_window_global(global_id):
            self.__relocate_to_active_global(global_id)


    def _is_active_window_global(self, global_id:str) -> bool:
        return global_id in self.global_running_stack and self.global_running_stack[0] == global_id

    def _is_running_global(self, global_id:str) -> bool:
        return global_id in self.global_running_stack

    def __relocate_to_active_global(self, global_id:str) -> None:
        current_index = self.global_running_stack.index(global_id)
        if current_index > 0:
            Shortcut.lx_cycle_windows(current_index, 2)
            self.global_running_stack.insert(0, self.global_running_stack.pop(current_index))

    def _remove_app_from_global_stack(self, global_id:str):
        self.global_running_stack.remove(global_id)