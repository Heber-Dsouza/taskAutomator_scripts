from classes.core.mouse import Mouse
from models.IN.beep_setting import BeepSetting

Mouse.get_position(3, True, BeepSetting(quantity=1, frequency=4))
