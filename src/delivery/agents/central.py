from maspy import *

class Central(Agent):
    def on_idle(self):
        self.stop_cycle()