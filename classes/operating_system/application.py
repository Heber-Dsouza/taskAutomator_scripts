import uuid
from classes.operating_system.gnome import Gnome
from classes.operating_system.shortcut import Shortcut
from classes.core.window import Window

class Application(Gnome):

    def __init_subclass__(cls):
        cls.global_id = str(uuid.uuid4())
        cls.running_stack = []

    def __init__(self, launch_command:str):
        super().__init__(launch_command)
        self.id=None

    def run(self):

        if self.is_running():
            self.open()
        else:
            self._launch(self.global_id)
            window_id = Window.get_active_window_id()
            self.running_stack.insert(0, window_id)

    def is_active_window(self) -> bool:
        return self._is_active_window_global(self.global_id) and self.id in self.running_stack and self.running_stack[0] == self.id

    def open(self):
        if not self.is_running():
            self.run()
        if not self.is_active_window():
            self.__relocate_to_active()

    def close(self):
        if self.is_running() and not self.is_active_window():
            self.__relocate_to_active()
        self._remove_app_from_stack(self.global_id)
        self.running_stack.remove(self.id)
        Window.close_active_window_by_id(self.id)


    def is_running(self) -> bool:
        return self.id in self.running_stack

    def __relocate_to_active(self) -> None:
        self._active_global(self.global_id)
        current_item_index = self.running_stack.index(self.id)
        if current_item_index > 0:
            Shortcut.lx_cycle_app_windows(current_item_index, 2)
            self.running_stack.insert(0, self.running_stack.pop(current_item_index))