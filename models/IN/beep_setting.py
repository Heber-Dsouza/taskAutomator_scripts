class BeepSetting:
    def __init__(self, quantity:int|None=3, frequency:float|None=0.3):
        """
       Stores beep configuration settings.

       Args:
           quantity (int | None, optional): Number of beeps to play. Defaults to 3.
           frequency (float | None, optional): Time interval between beeps in seconds. Defaults to 0.3.
       """
        self.quantity = quantity
        self.frequency = frequency