from maspy import *

class Driver(Agent):
    def on_idle(self):
        self.stop_cycle()