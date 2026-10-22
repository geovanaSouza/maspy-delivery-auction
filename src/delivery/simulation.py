from maspy import *

from delivery.agents.driver import Driver
from delivery.agents.central import Central
from delivery.config import DRV_SETTINGS

def main():
    Channel().show_exec = True

    for i in range (0,3):
        Driver("driver", DRV_SETTINGS["region"][i])

    Central("central")
    Admin().start_system()