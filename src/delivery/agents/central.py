from maspy import *

class Central(Agent):
    def __init__(self, agt_name):
        super().__init__(agt_name)
        self.add(Goal("request_driver"))

    @pl(gain, Goal("request_driver"))
    def request_driver(self, src):
        self.send(broadcast, achieve, Goal("analyze_offer", "south"))

    @pl(gain, Belief("match_region", Any))
    def receive_answer(self, src, driver):
        self.print(f"Driver answer: {driver}")
        self.stop_cycle()