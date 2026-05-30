class DetailedDelays:
    def __init__(
            self, delay_terminal:float|int,
            delay_typing:float|int,
            delay_confirm:float|int,
            post_wait_delay:float|int
    ):
        """
        Stores detailed delay settings used during terminal automation.

        Args:
            delay_terminal (float | int): Time to wait before opening the terminal.
            delay_typing (float | int): Time to wait before typing the command.
            delay_confirm (float | int): Time to wait before confirming the command (pressing Enter).
            post_wait_delay (float | int): Time to wait after confirming the command.
        """
        self.delay_terminal = delay_terminal
        self.delay_typing = delay_typing
        self.delay_confirm = delay_confirm
        self.post_wait_delay = post_wait_delay