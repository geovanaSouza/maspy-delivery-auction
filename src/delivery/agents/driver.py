from maspy import *

class Driver(Agent):
    def __init__(self, agt_name, region):
        super().__init__(agt_name)
        self.add(Belief("region", region))
        self.print(f"Agent {self.my_name}: region ({region})")

    @pl(gain, Goal("analyze_offer", Any))
    def analyze_offer(self, src, offer_region):
        self.print("Analyzing deliver match reagion")
        self.test(Belief("offer_region", offer_region))

    @pl(test, Belief("offer_region", Any), Belief("region", Any))
    def check_match_region(self, src, offer_region, driver_region):
        if offer_region == driver_region:
            self.send("central", tell, Belief("match_region", self.my_name))
        self.stop_cycle()