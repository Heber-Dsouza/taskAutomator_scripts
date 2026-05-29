import time
from abc import ABC
from ewmh.ewmh import EWMH
from typing import Final

class Window(ABC):

    def __init__(self):
        self.__win_manager = EWMH()

    def _get_active_window_properties(self):
        return self.__win_manager.getActiveWindow()

    def _get_active_window_id(self):
        return self.__win_manager.getActiveWindow().id

    def _close_active_window_by_id(self, delay:float|int|None):
        default_delay_time:Final = 1.0
        time.sleep(delay or default_delay_time)

        window_id = self._get_active_window_id()
        self.__win_manager.setCloseWindow(window_id)
        self.__win_manager.display.flush()