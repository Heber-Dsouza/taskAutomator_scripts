from ewmh.ewmh import EWMH

class Window:
    __window_instance = EWMH()

    @staticmethod
    def get_active_window_properties():
        return Window.__window_instance.getActiveWindow()

    @staticmethod
    def get_active_window_id():
        return Window.__window_instance.getActiveWindow().id

    @staticmethod
    def close_active_window_by_id(window_id:str):
        return Window.__window_instance.setCloseWindow(window_id)