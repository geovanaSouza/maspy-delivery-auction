from maspy import *

from delivery.agents.driver import Driver
from delivery.agents.central import Central

def main():
    for i in range (1,3):
        Driver("driver")

    Central("central")
    Admin().start_system()