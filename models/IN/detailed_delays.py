class DetailedDelays:
    def __init__(
            self, delay_terminal:float|int,
            delay_typing:float|int,
            delay_confirm:float|int,
            post_wait_delay:float|int
    ):
        self.delay_terminal = delay_terminal
        self.delay_typing = delay_typing
        self.delay_confirm = delay_confirm
        self.post_wait_delay = post_wait_delay