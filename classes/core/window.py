from abc import ABC
from ewmh.ewmh import EWMH

class Window(ABC):

    def __init__(self):
        self.__win_manager = EWMH()

    def _get_active_window_properties(self):
        return self.__win_manager.getActiveWindow()

    def _get_active_window_id(self):
        return self.__win_manager.getActiveWindow().id

    def _close_active_window_by_id(self, window_id:str):
        return self.__win_manager.setCloseWindow(window_id)