import uuid
from classes.operating_system.gnome import Gnome
from classes.operating_system.shortcut import Shortcut

class Application(Gnome):
    running_stack: list[str] = []

    def __init__(self, launch_command:str):
        super().__init__(launch_command)
        self.id = str(uuid.uuid4())

    def run(self):

        if self.is_running():
            self.open()
        else:
            self._launch(self.global_id)
            self.running_stack.insert(0, self.id)

    def is_active_window(self) -> bool:
        return self._is_active_window_global() and self.id in self.running_stack and self.running_stack[0] == self.id

    def open(self):
        if not self.is_active_window():
            self.__relocate_to_active()

    def is_running(self) -> bool:
        return self.id in self.running_stack

    def __relocate_to_active(self) -> None:
        if not self._is_running_global():
            self._active_global()
        current_item_index = self.running_stack.index(self.id)
        Shortcut.lx_cycle_app_windows(current_item_index, 2)
        self.running_stack.insert(0, self.running_stack.pop(current_item_index))